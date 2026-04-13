# Evaluation Rubric

Use this rubric together with [`core/eval-cases.md`](./eval-cases.md) when comparing prompt revisions, model variants, or platform adapters.

The goal is to keep evaluation lightweight and repeatable without turning it into a heavy benchmarking framework.

## Rating Scale

Score each criterion for each case as:

- `2` = pass
- `1` = soft fail
- `0` = hard fail

Use the scores conservatively:

- `2` means the behavior is clearly acceptable for the case
- `1` means the result is usable but needs revision or tighter prompt control
- `0` means the result breaks an important requirement of the skill

## Core Criteria

Score these six criteria for every case:

1. Meaning preservation
2. No invented facts, motivation, or detail
3. Natural Russian business tone
4. Removal of AI phrasing, bureaucracy, and template language where relevant
5. No over-editing
6. No drift into casual, promotional, or synthetic tone

Maximum score per case: `12`

## How To Interpret Results

### Case-Level Decision

- `Ready`: total score `11-12`, with no `0`
- `Needs revision`: total score `8-10`, with no `0` in criteria 1-2
- `Fail`: any `0` in criteria 1-2, or total score `0-7`

Treat criteria `1` and `2` as non-negotiable. A result that changes meaning or invents facts should fail even if the wording sounds good.

### Run-Level Decision

When reviewing a full set of cases:

- `Strong`: no failed cases and most cases are `Ready`
- `Borderline`: no critical failures, but several cases are `Needs revision`
- `Not ready`: one or more failed cases, especially on meaning preservation or invented detail

## Soft Fail vs Hard Fail

Use `1` when the issue is noticeable but limited:

- slightly too smooth
- a bit drier than the source
- some template language remains
- a useful sentence was made weaker but not factually wrong

Use `0` when the issue breaks the contract of the skill:

- meaning changed
- new motivation or achievements appeared
- technical requirement became less precise
- tone turned promotional, recruiter-template-like, or obviously synthetic
- a previously natural text was over-edited into something weaker

## Quick Evaluation Template

Use this compact template when logging results:

```text
Case:
Total:
Decision: Ready / Needs revision / Fail

Scores:
1. Meaning preservation:
2. No invented facts or detail:
3. Natural business tone:
4. Pattern removal:
5. No over-editing:
6. No tone drift:

Notes:
```

## Suggested Use

- Use `core/eval-cases.md` for the scenario set
- Use this rubric for scoring consistency
- Add short notes only where a score is not obviously a `2`
- Prefer comparing variants on the same cases instead of adding many weak cases

This rubric is intentionally lightweight. It is meant to improve comparison discipline, not to replace editorial judgment.
