# Установка skill в Codex

Этот адаптер устанавливается в Codex как обычный skill.

Имя skill-а: `humanize-russian-business-text`

## Вариант 1. Репозиторий уже на компьютере

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills\humanize-russian-business-text" | Out-Null
Copy-Item -Recurse -Force ".\adapters\skill\*" "$HOME\.codex\skills\humanize-russian-business-text\"
```

macOS / Linux:

```bash
mkdir -p ~/.codex/skills/humanize-russian-business-text
cp -R ./adapters/skill/* ~/.codex/skills/humanize-russian-business-text/
```

## Вариант 2. Сначала клонировать репозиторий

Windows PowerShell:

```powershell
git clone https://github.com/ValentinAvramko/editorial-skill-for-natural-russian-business-writing.git
cd editorial-skill-for-natural-russian-business-writing
New-Item -ItemType Directory -Force "$HOME\.codex\skills\humanize-russian-business-text" | Out-Null
Copy-Item -Recurse -Force ".\adapters\skill\*" "$HOME\.codex\skills\humanize-russian-business-text\"
```

macOS / Linux:

```bash
git clone https://github.com/ValentinAvramko/editorial-skill-for-natural-russian-business-writing.git
cd editorial-skill-for-natural-russian-business-writing
mkdir -p ~/.codex/skills/humanize-russian-business-text
cp -R ./adapters/skill/* ~/.codex/skills/humanize-russian-business-text/
```

После копирования перезапустите Codex, если skill не появился сразу.

## Что должно получиться

В каталоге `~/.codex/skills/humanize-russian-business-text/` должны лежать:

- `SKILL.md`
- `adapter.yaml`
- `references/patterns.md`
- `references/examples.md`
- `targets/codex/agents/openai.yaml`

## Как вызывать

Простой вариант:

```text
Используй $humanize-russian-business-text и перепиши этот текст:

[ваш текст]
```

Более точный вариант:

```text
Используй $humanize-russian-business-text.
Это сопроводительное письмо.
Нужно убрать нейрояз и карьерные штампы, но сохранить спокойный профессиональный тон.
Если текст уже нормальный, правь минимально.
Верни только итоговый вариант.

[ваш текст]
```
