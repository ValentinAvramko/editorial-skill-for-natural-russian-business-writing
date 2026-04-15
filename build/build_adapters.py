#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CORE_DIR = ROOT / "core"
ADAPTERS_DIR = ROOT / "adapters"
PROMPT_DIR = ADAPTERS_DIR / "prompt"

PROMPT_SPEC_PATH = CORE_DIR / "prompt-spec.md"
PATTERNS_PATH = CORE_DIR / "patterns.md"
EXAMPLES_PATH = CORE_DIR / "examples.md"

SKILL_PATH = ADAPTERS_DIR / "skill" / "SKILL.md"
PROMPT_PORTABLE_PATH = PROMPT_DIR / "humanize-russian-business-text.prompt.md"
PROMPT_INSTRUCTIONS_PATH = PROMPT_DIR / "humanize-russian-business-text.instructions.md"
PROMPT_PATTERNS_PATH = PROMPT_DIR / "humanize-russian-business-text.patterns.md"
PROMPT_EXAMPLES_PATH = PROMPT_DIR / "humanize-russian-business-text.examples.md"

SYNC_TARGETS = {
    ADAPTERS_DIR / "skill" / "references" / "patterns.md": PATTERNS_PATH,
    ADAPTERS_DIR / "skill" / "references" / "examples.md": EXAMPLES_PATH,
    PROMPT_PATTERNS_PATH: PATTERNS_PATH,
    PROMPT_EXAMPLES_PATH: EXAMPLES_PATH,
}

SECTION_ORDER = [
    "Назначение",
    "Когда использовать",
    "Целевой стиль",
    "Рабочий процесс",
    "Базовые правила",
    "Жанровые ориентиры",
    "Жесткие ограничения",
    "Финальная проверка",
    "Правило выдачи",
]

SKILL_FRONTMATTER = """---
name: humanize-russian-business-text
description: Приводи русскоязычный деловой текст к естественному, человеческому и профессиональному звучанию без нейрояза, канцелярита, корпоративного жаргона и шаблонных AI-формул. Используй этот skill при редактировании писем, сопроводительных писем, откликов, самопрезентаций, деловой переписки, коротких рабочих сообщений, описаний кейсов и проектов, технических требований и тестовых заданий, когда текст должен звучать по-русски естественно, ясно и уместно, но без фамильярности, лести и машинной гладкости.
---
"""

SKILL_INTRO = """# Humanize Russian Business Text
"""

PROMPT_TITLE = "# Редакторская спецификация"

SKILL_REFERENCES_SECTION = """## Локальные reference-файлы

Этот skill использует локальные справочники как дополнительную калибровку, а не как источник новой редакторской политики.

Открывай их по триггерам:

- `references/patterns.md`: когда видишь AI-штампы, важничание, канцелярит, корпоративный жаргон, карьерный шаблон, слишком гладкий тон или риск переисправления.
- `references/examples.md`: когда работаешь с письмами, откликами, сообщениями рекрутерам, самопрезентациями, короткими рабочими сообщениями и пограничными случаями, где важно удержать глубину вмешательства.

Не копируй reference-примеры механически. Используй их как ориентир по тону, плотности и глубине редактуры.
"""

PROMPT_REFERENCES_SECTION = """## Локальные reference-файлы

Если в контексте доступны файлы `humanize-russian-business-text.patterns.md` и `humanize-russian-business-text.examples.md`, используй их как прямой reference-слой.

Открывай их по триггерам:

- `humanize-russian-business-text.patterns.md`: когда видишь AI-штампы, важничание, канцелярит, корпоративный жаргон, карьерный шаблон, слишком гладкий тон или риск переисправления.
- `humanize-russian-business-text.examples.md`: когда работаешь с письмами, откликами, сообщениями рекрутерам, самопрезентациями, короткими рабочими сообщениями и пограничными случаями, где важно удержать глубину вмешательства.

Если этих файлов нет в чате, проекте или Gem, продолжай работать по этому prompt без них.

Не копируй reference-примеры механически. Используй их как ориентир по тону, плотности и глубине редактуры.
"""

PROMPT_INSTRUCTIONS_TEXT = """# Humanize Russian Business Text

## Обязательный prompt-файл

Файл `humanize-russian-business-text.prompt.md` обязателен и является главным файлом редакторской спецификации для этого адаптера.

Всегда:

1. сначала открой `humanize-russian-business-text.prompt.md`;
2. следуй ему полностью как основному prompt-слою;
3. не подменяй его своей краткой интерпретацией и не пересказывай его правила заново по памяти.

Если `humanize-russian-business-text.prompt.md` недоступен в knowledge / files / sources, не заменяй его сокращённой версией из этих instructions. Вместо этого попроси подключить этот файл.

## Reference-файлы

Если вместе с prompt-файлом доступны `humanize-russian-business-text.patterns.md` и `humanize-russian-business-text.examples.md`, используй их только как reference-слой к основному prompt.

Вызывай их по триггерам, которые описаны в `humanize-russian-business-text.prompt.md`.

Не копируй примеры механически. Используй их как ориентир по тону, плотности и глубине редактуры.

## Правило ответа

По умолчанию возвращай только итоговый отредактированный текст.

Если платформа склонна добавлять объяснения по умолчанию, всё равно держись правила из `humanize-russian-business-text.prompt.md`: без мета-комментариев, если пользователь их явно не просил.
"""


@dataclass(frozen=True)
class RenderedFile:
    path: Path
    content: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def parse_prompt_spec_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_title: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_lines
        if current_title is None:
            return
        body = "\n".join(current_lines).strip()
        sections[current_title] = body
        current_title = None
        current_lines = []

    for line in normalize_newlines(text).splitlines():
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            flush()
            current_title = line[3:].strip()
            continue
        if current_title is not None:
            current_lines.append(line)

    flush()
    missing = [title for title in SECTION_ORDER if title not in sections]
    if missing:
        missing_titles = ", ".join(missing)
        raise ValueError(f"В `core/prompt-spec.md` не найдены обязательные секции: {missing_titles}")
    return sections


def render_section(title: str, body: str) -> str:
    return f"## {title}\n\n{body.strip()}\n"


def render_prompt(sections: dict[str, str]) -> str:
    blocks = [PROMPT_TITLE, ""]

    for title in SECTION_ORDER:
        blocks.append(render_section(title, sections[title]).strip())
        blocks.append("")
        if title == "Жесткие ограничения":
            blocks.append(PROMPT_REFERENCES_SECTION.strip())
            blocks.append("")

    return ensure_trailing_newline("\n".join(blocks).strip())


def render_skill(sections: dict[str, str]) -> str:
    blocks = [SKILL_FRONTMATTER.strip(), "", SKILL_INTRO.strip(), ""]

    for title in SECTION_ORDER:
        blocks.append(render_section(title, sections[title]).strip())
        blocks.append("")
        if title == "Жесткие ограничения":
            blocks.append(SKILL_REFERENCES_SECTION.strip())
            blocks.append("")

    return ensure_trailing_newline("\n".join(blocks).strip())


def render_prompt_instructions(sections: dict[str, str]) -> str:
    return ensure_trailing_newline(PROMPT_INSTRUCTIONS_TEXT.strip())


def ensure_trailing_newline(text: str) -> str:
    return text.rstrip() + "\n"


def build_expected_files() -> list[RenderedFile]:
    prompt_spec = read_text(PROMPT_SPEC_PATH)
    sections = parse_prompt_spec_sections(prompt_spec)
    rendered_prompt = render_prompt(sections)
    rendered = [
        RenderedFile(SKILL_PATH, render_skill(sections)),
        RenderedFile(PROMPT_PORTABLE_PATH, rendered_prompt),
        RenderedFile(PROMPT_INSTRUCTIONS_PATH, render_prompt_instructions(sections)),
    ]

    for target, source in SYNC_TARGETS.items():
        rendered.append(RenderedFile(target, ensure_trailing_newline(normalize_newlines(read_text(source)).strip())))
    return rendered


def sync_files(files: list[RenderedFile]) -> int:
    changed = 0
    for rendered in files:
        current = (
            ensure_trailing_newline(normalize_newlines(rendered.path.read_text(encoding="utf-8-sig")).strip())
            if rendered.path.exists()
            else None
        )
        if current != rendered.content:
            rendered.path.parent.mkdir(parents=True, exist_ok=True)
            rendered.path.write_text(rendered.content, encoding="utf-8")
            print(f"updated {to_repo_relative(rendered.path)}")
            changed += 1
        else:
            print(f"ok {to_repo_relative(rendered.path)}")
    print(f"sync complete: {changed} file(s) updated")
    return 0


def check_files(files: list[RenderedFile]) -> int:
    drifted: list[str] = []
    for rendered in files:
        current = (
            ensure_trailing_newline(normalize_newlines(rendered.path.read_text(encoding="utf-8-sig")).strip())
            if rendered.path.exists()
            else ""
        )
        if current != rendered.content:
            drifted.append(to_repo_relative(rendered.path))

    if drifted:
        print("drift detected:")
        for path in drifted:
            print(f"- {path}")
        print("run `python build/build_adapters.py sync` to refresh the generated adapter files.")
        return 1

    print("adapter artifacts are in sync")
    return 0


def to_repo_relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Собрать производные adapter-файлы из core и проверить drift."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync_parser = subparsers.add_parser(
        "sync", help="Пересобрать prompt/skill entrypoint-файлы и reference-артефакты."
    )
    sync_parser.set_defaults(func=command_sync)

    check_parser = subparsers.add_parser(
        "check", help="Проверить, что производные adapter-файлы синхронизированы."
    )
    check_parser.set_defaults(func=command_check)
    return parser


def command_sync(_: argparse.Namespace) -> int:
    return sync_files(build_expected_files())


def command_check(_: argparse.Namespace) -> int:
    return check_files(build_expected_files())


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
