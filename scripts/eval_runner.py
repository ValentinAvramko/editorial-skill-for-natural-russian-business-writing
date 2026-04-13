#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = ROOT / "core" / "eval-cases.md"
RUBRIC_PATH = ROOT / "core" / "eval-rubric.md"

CASE_PATTERN = re.compile(r"^## Кейс (\d+)\. (.+)$")

CRITERIA = [
    ("meaning_preserved", "Сохранение смысла"),
    ("no_invented_details", "Нет выдуманных фактов и деталей"),
    ("business_tone", "Естественный деловой тон"),
    ("patterns_removed", "Удаление паттернов"),
    ("no_overediting", "Нет переисправления"),
    ("no_tone_drift", "Нет ухода тона"),
]

DECISION_READY = "Готово"
DECISION_NEEDS_WORK = "Нужна доработка"
DECISION_FAIL = "Провал"

RUN_DECISION_STRONG = "Сильно"
RUN_DECISION_BORDERLINE = "Погранично"
RUN_DECISION_NOT_READY = "Не готово"


@dataclass
class EvalCase:
    case_id: int
    title: str
    input_text: str
    expected_behavior: list[str]


def load_cases(path: Path = CASES_PATH) -> list[EvalCase]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    cases: list[EvalCase] = []
    current_id: int | None = None
    current_title: str | None = None
    current_section: str | None = None
    input_lines: list[str] = []
    expected_behavior: list[str] = []

    def flush_case() -> None:
        nonlocal current_id, current_title, current_section, input_lines, expected_behavior
        if current_id is None or current_title is None:
            return
        input_text = "\n".join(trim_blank_edges(input_lines)).strip()
        cases.append(
            EvalCase(
                case_id=current_id,
                title=current_title,
                input_text=input_text,
                expected_behavior=expected_behavior[:],
            )
        )
        current_id = None
        current_title = None
        current_section = None
        input_lines = []
        expected_behavior = []

    for line in lines:
        case_match = CASE_PATTERN.match(line)
        if case_match:
            flush_case()
            current_id = int(case_match.group(1))
            current_title = case_match.group(2).strip()
            continue

        if current_id is None:
            continue

        if line == "### Вход":
            current_section = "input"
            continue

        if line == "### Ожидаемое поведение":
            current_section = "expected"
            continue

        if line.startswith("### "):
            current_section = None
            continue

        if current_section == "input":
            input_lines.append(line)
            continue

        if current_section == "expected":
            if line.startswith("- "):
                expected_behavior.append(line[2:].strip())
            elif line.strip() and expected_behavior:
                expected_behavior[-1] = f"{expected_behavior[-1]} {line.strip()}"

    flush_case()
    return cases


def trim_blank_edges(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def make_template_case(case: EvalCase) -> dict[str, Any]:
    return {
        "case_id": case.case_id,
        "title": case.title,
        "input": case.input_text,
        "expected_behavior": case.expected_behavior,
        "candidate_output": "",
        "scores": {key: None for key, _ in CRITERIA},
        "notes": "",
    }


def command_export_cases(args: argparse.Namespace) -> int:
    cases = [make_template_case(case) for case in load_cases()]
    payload = {
        "cases_source": to_repo_relative(CASES_PATH),
        "rubric_source": to_repo_relative(RUBRIC_PATH),
        "exported_at": utc_now_iso(),
        "cases": cases,
    }
    write_json(Path(args.output), payload)
    return 0


def command_init_run(args: argparse.Namespace) -> int:
    cases = [make_template_case(case) for case in load_cases()]
    payload = {
        "run_name": args.name,
        "target": args.target,
        "created_at": utc_now_iso(),
        "cases_source": to_repo_relative(CASES_PATH),
        "rubric_source": to_repo_relative(RUBRIC_PATH),
        "summary_notes": "",
        "cases": cases,
    }
    write_json(Path(args.output), payload)
    return 0


def command_report(args: argparse.Namespace) -> int:
    run_path = Path(args.input)
    payload = json.loads(run_path.read_text(encoding="utf-8-sig"))
    reports = build_case_reports(payload.get("cases", []))
    run_decision = decide_run(reports)
    report_text = render_report(payload, reports, run_decision)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report_text, encoding="utf-8")
    else:
        print(report_text)
    return 0


def build_case_reports(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    reports: list[dict[str, Any]] = []
    for case in cases:
        case_id = case.get("case_id")
        title = case.get("title")
        scores_raw = case.get("scores", {})
        scores: dict[str, int] = {}

        for key, label in CRITERIA:
            value = scores_raw.get(key)
            if value not in (0, 1, 2):
                raise ValueError(
                    f"Кейс {case_id}: критерий '{label}' должен быть 0, 1 или 2, сейчас: {value!r}"
                )
            scores[key] = int(value)

        total = sum(scores.values())
        decision = decide_case(scores, total)
        reports.append(
            {
                "case_id": case_id,
                "title": title,
                "scores": scores,
                "total": total,
                "decision": decision,
                "notes": case.get("notes", ""),
            }
        )
    return reports


def decide_case(scores: dict[str, int], total: int) -> str:
    if scores["meaning_preserved"] == 0 or scores["no_invented_details"] == 0:
        return DECISION_FAIL
    if 11 <= total <= 12 and 0 not in scores.values():
        return DECISION_READY
    if 8 <= total <= 10:
        return DECISION_NEEDS_WORK
    return DECISION_FAIL


def decide_run(reports: list[dict[str, Any]]) -> str:
    failed = sum(1 for report in reports if report["decision"] == DECISION_FAIL)
    ready = sum(1 for report in reports if report["decision"] == DECISION_READY)
    total = len(reports)

    if failed > 0:
        return RUN_DECISION_NOT_READY
    if ready > total / 2:
        return RUN_DECISION_STRONG
    return RUN_DECISION_BORDERLINE


def render_report(
    payload: dict[str, Any], reports: list[dict[str, Any]], run_decision: str
) -> str:
    total_cases = len(reports)
    ready = sum(1 for report in reports if report["decision"] == DECISION_READY)
    needs_work = sum(1 for report in reports if report["decision"] == DECISION_NEEDS_WORK)
    failed = sum(1 for report in reports if report["decision"] == DECISION_FAIL)
    total_score = sum(report["total"] for report in reports)
    max_score = total_cases * len(CRITERIA) * 2
    average_score = total_score / total_cases if total_cases else 0.0

    lines = [
        "# Отчёт по eval-прогону",
        "",
        f"- Прогон: {payload.get('run_name') or 'без названия'}",
        f"- Цель: {payload.get('target') or 'не указана'}",
        f"- Кейсы: {payload.get('cases_source') or to_repo_relative(CASES_PATH)}",
        f"- Рубрика: {payload.get('rubric_source') or to_repo_relative(RUBRIC_PATH)}",
        f"- Решение по прогону: {run_decision}",
        f"- Суммарный балл: {total_score}/{max_score}",
        f"- Средний балл за кейс: {average_score:.2f}",
        "",
        "## Сводка",
        "",
        f"- `Готово`: {ready}",
        f"- `Нужна доработка`: {needs_work}",
        f"- `Провал`: {failed}",
        "",
        "## Кейсы",
        "",
        "| Кейс | Итог | Решение |",
        "| --- | ---: | --- |",
    ]

    for report in reports:
        lines.append(
            f"| {report['case_id']}. {report['title']} | {report['total']}/12 | {report['decision']} |"
        )

    notes_with_content = [report for report in reports if str(report["notes"]).strip()]
    if notes_with_content:
        lines.extend(["", "## Заметки", ""])
        for report in notes_with_content:
            lines.append(
                f"- Кейс {report['case_id']}. {report['title']}: {str(report['notes']).strip()}"
            )

    return "\n".join(lines) + "\n"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def to_repo_relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Лёгкий eval-runner поверх core/eval-cases.md и core/eval-rubric.md."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_cases = subparsers.add_parser(
        "export-cases",
        help="Выгрузить кейсы из core/eval-cases.md в JSON.",
    )
    export_cases.add_argument("--output", required=True, help="Путь к JSON-файлу.")
    export_cases.set_defaults(func=command_export_cases)

    init_run = subparsers.add_parser(
        "init-run",
        help="Создать шаблон eval-прогона с кейсами и пустыми оценками.",
    )
    init_run.add_argument("--name", default="manual-eval", help="Название прогона.")
    init_run.add_argument(
        "--target",
        default="",
        help="Что именно оценивается: модель, адаптер или версия промпта.",
    )
    init_run.add_argument("--output", required=True, help="Путь к JSON-файлу прогона.")
    init_run.set_defaults(func=command_init_run)

    report = subparsers.add_parser(
        "report",
        help="Проверить оценки и собрать markdown-отчёт по прогону.",
    )
    report.add_argument("--input", required=True, help="Путь к JSON-файлу прогона.")
    report.add_argument("--output", help="Куда сохранить markdown-отчёт.")
    report.set_defaults(func=command_report)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except ValueError as error:
        parser.error(str(error))
    except FileNotFoundError as error:
        parser.error(f"Не найден файл: {error.filename}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
