# Editorial Skill for Natural Russian Business Writing

This repository contains a reusable editorial specification for rewriting Russian-language business text so it sounds natural, clear, professional, and human.

It is meant for cases where a text feels AI-generated, overly polished, bureaucratic, template-like, or corporately empty, but still needs to stay business-appropriate and factually intact.

## What This Is

This is not just a single prompt.

It is a small editorial system with:

- a platform-neutral core specification
- reusable pattern and example references
- a Codex adapter based on the working skill implementation

## What It Helps With

Use it for:

- cover letters
- job application responses
- recruiter messages
- business correspondence
- short work messages
- self-presentations
- project descriptions
- case descriptions
- technical requirements
- test assignments

## Editorial Goal

The goal is to make Russian business writing sound:

- natural
- clear
- specific
- calm
- professional
- human

without turning it into:

- bureaucratic text
- ad copy
- recruiter-template language
- corporate jargon
- synthetic “AI polish”
- overly casual conversation

## Principles

- Preserve meaning, facts, and intent.
- Improve style, clarity, rhythm, and wording, not the underlying content.
- Do not invent experience, motivation, numbers, achievements, timelines, or emotional framing.
- Edit minimally when the source already sounds natural.
- Do not replace one template with another.

## Repository Structure

```text
editorial-skill-for-natural-russian-business-writing/
├─ README.md
├─ LICENSE
├─ core/
│  ├─ prompt-spec.md
│  ├─ patterns.md
│  └─ examples.md
└─ adapters/
   └─ codex/
      ├─ SKILL.md
      ├─ agents/
      │  └─ openai.yaml
      └─ references/
         ├─ patterns.md
         └─ examples.md
```

## How To Use

### Generic LLM / Manual Use

Use [`core/prompt-spec.md`](./core/prompt-spec.md) as:

- a system prompt
- a custom instruction block
- an agent profile
- a reusable editorial policy in your own workflow

The main specification is in Russian: [`core/prompt-spec.md`](./core/prompt-spec.md).

An English companion version is available here: [`core/prompt-spec.en.md`](./core/prompt-spec.en.md).

Use [`core/patterns.md`](./core/patterns.md) and [`core/examples.md`](./core/examples.md) as supporting reference files.

### Codex Use

Use the adapter in [`adapters/codex`](./adapters/codex/), which contains the working Codex skill package:

- `SKILL.md`
- `agents/openai.yaml`
- `references/patterns.md`
- `references/examples.md`

## Language

The repository documentation is in English so the project is easier to publish and reuse across tools.

The main editorial specification is in Russian because the skill operates on Russian-language business writing and the style constraints are more precise in the working language.

An English version of the prompt spec is included alongside it for portability and reference.

## Current Status

This version is ready to use as a working base.

Further improvements are optional and mostly about refinement, not missing fundamentals. The most useful future additions would be:

1. platform-neutral evaluation cases
2. more technical before/after examples
3. adapters for other platforms

## Positioning

Treat this repository as an editorial skill for natural Russian business writing, not as a one-off prompt.
