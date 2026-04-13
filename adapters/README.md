# Adapters Guide

This file defines the source of truth and synchronization rules between the platform-neutral core and platform-specific adapters.

Use it when updating `core/`, adding a new adapter, or deciding whether a change belongs in the core specification or in an adapter layer.

## Source Of Truth

The source of truth for editorial behavior is `core/`.

That includes:

- `core/prompt-spec.md`
- `core/prompt-spec.en.md`
- `core/patterns.md`
- `core/examples.md`
- `core/eval-cases.md`
- `core/eval-rubric.md`

If an adapter conflicts with the core on editorial logic, constraints, or target style, the core wins.

## What Adapters Are Allowed To Change

Adapters may translate the core into platform-native packaging.

That can include:

- skill metadata and front matter
- agent manifests and platform config files
- file layout required by the platform
- instructions about when to open local reference files
- small wording changes that improve compatibility with a specific tool
- condensed or reorganized reference material when the platform benefits from shorter local files

These are delivery-layer changes, not editorial-policy changes.

## What Adapters Must Preserve

Every adapter must preserve the core contract:

- meaning preservation over stylistic invention
- no invented facts, motivation, achievements, timelines, or emotional color
- natural Russian business tone
- resistance to bureaucracy, recruiter-template language, corporate jargon, and synthetic polish
- minimal editing when the source is already good
- protection of technical precision in requirements, cases, and test tasks
- avoidance of replacing one template with another

An adapter must not silently soften hard constraints just because a platform prefers shorter instructions.

## Reference File Policy

Adapter reference files may be:

- direct copies of the corresponding core files
- shortened working copies derived from the core
- platform-specific rearrangements of the same material

But they must not introduce a different editorial standard.

For the current Codex adapter:

- `adapters/codex/references/patterns.md` should stay aligned with the detection logic of `core/patterns.md`
- `adapters/codex/references/examples.md` should stay aligned with the intervention style of `core/examples.md`
- `adapters/codex/SKILL.md` may add platform workflow instructions, but should not override core editorial rules

## Update Rule

When the editorial policy changes, update the core first.

Then review every adapter and decide whether it needs:

1. no change
2. a wording sync
3. a reference-file refresh
4. a platform-config update

Do not start by patching an adapter in isolation if the change is actually editorial.

## Practical Sync Checklist

Use this checklist after meaningful core changes:

1. Confirm whether the change affects editorial behavior, examples, pattern detection, or evaluation.
2. Update the relevant file in `core/` first.
3. Review `adapters/codex/SKILL.md` for wording that now drifts from the core.
4. Review `adapters/codex/references/` for outdated examples or pattern lists.
5. Check whether the adapter still points to the right local reference files.
6. Re-run spot checks against `core/eval-cases.md` and `core/eval-rubric.md` if the change is behaviorally meaningful.

## When A Change Belongs In Core

Put the change in `core/` if it affects:

- target tone
- hard constraints
- allowed vs forbidden rewriting behavior
- genre guidance
- evaluation expectations
- pattern taxonomy
- example philosophy

## When A Change Belongs In An Adapter

Put the change in an adapter if it affects:

- packaging for a specific tool
- platform-specific metadata
- invocation wording for a given agent environment
- reference loading instructions
- format constraints imposed by the platform

## Current Repository Rule

In this repository, `core/` defines the editorial standard and `adapters/` packages that standard for execution environments.

Treat adapters as faithful implementations of the core, not as independent prompt branches.
