# Editorial Skill for Natural Russian Business Writing

This repository contains an editorial skill and prompt-engineering toolkit for rewriting Russian-language business text so it sounds natural, clear, professional, and human.

Use it when a text feels AI-generated, overly polished, bureaucratic, template-like, or corporately empty, but still needs to stay business-appropriate, precise, and factually intact.

The project combines two things:

- an editorial framework for natural Russian business writing
- a reusable AI-ready specification with reference patterns, examples, evaluation cases, and a Codex adapter

## Why This Exists

Generic “humanizer” prompts often do one of two things badly:

- they smooth the text but make it emptier, more generic, or more synthetic
- they make the text sound more casual or “alive” at the cost of precision, business tone, or factual discipline

This project exists to solve a narrower and more practical problem: Russian business writing often needs not softer wording, but disciplined editorial rewriting. That means removing AI phrasing, bureaucracy, recruiter-template language, and synthetic polish while preserving meaning, intent, constraints, and professional tone.

The goal is not to decorate text. The goal is to make it read like it was written by a competent professional person.

## How It Differs From Generic Humanizers

This repository is stricter and more editorial than a typical “make it sound human” prompt.

It is designed to:

- preserve facts, intent, and business logic
- avoid invented motivation, achievements, or emotional color
- protect technical precision in requirements, project descriptions, and test tasks
- prevent over-editing when the source is already good
- detect not only obvious AI phrasing, but also subtler markers like synthetic smoothness, recruiter-template tone, empty abstraction, and over-correct rhythm

It also treats humanization as a system rather than a one-off prompt:

- core specification
- pattern reference
- examples reference
- evaluation cases
- platform adapter

So the project is less about “making text nicer” and more about creating a reusable editorial standard for natural Russian business writing.

## What This Is

This is not just a single prompt or a style note.

It is a small editorial system with:

- a platform-neutral core specification
- reusable pattern and example references
- evaluation cases for comparing revisions
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

## Who This Is For

- people who write professional text in Russian
- candidates working on responses, cover letters, and recruiter communication
- managers, leads, and specialists who edit business communication
- teams building AI workflows for Russian-language business writing
- prompt engineers who want a reusable editorial spec rather than a one-off prompt

## Who This Is Not For

- people looking for a generic “make it warmer” prompt
- creative writing or brand-voice writing where invention matters more than factual discipline
- casual chat rewriting
- SEO rewriting
- sales copy generation
- users who want the system to invent motivation, achievements, or narrative color

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

In practice, this means editing for tone, rhythm, and clarity without inventing facts, diluting meaning, or replacing one template with another.

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

This version is ready to use.

Further improvements are optional and mostly about refinement, not missing fundamentals. The most useful future additions would be:

1. platform-neutral evaluation cases
2. more technical before/after examples
3. adapters for other platforms

## Positioning

Treat this repository as an editorial skill for natural Russian business writing, not as a one-off prompt.
