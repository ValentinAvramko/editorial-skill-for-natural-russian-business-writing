# Установка skill в Claude Code

Этот адаптер устанавливается в Claude Code как обычный skill.

Имя skill-а: `humanize-russian-business-text`

## Вариант 1. Репозиторий уже на компьютере

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills\humanize-russian-business-text" | Out-Null
Copy-Item -Recurse -Force ".\adapters\skill\*" "$HOME\.claude\skills\humanize-russian-business-text\"
```

macOS / Linux:

```bash
mkdir -p ~/.claude/skills/humanize-russian-business-text
cp -R ./adapters/skill/* ~/.claude/skills/humanize-russian-business-text/
```

После копирования перезапустите Claude Code, если skill не появился сразу.

## Вариант 2. Сначала клонировать репозиторий

Windows PowerShell:

```powershell
git clone https://github.com/ValentinAvramko/editorial-skill-for-natural-russian-business-writing.git
cd editorial-skill-for-natural-russian-business-writing
New-Item -ItemType Directory -Force "$HOME\.claude\skills\humanize-russian-business-text" | Out-Null
Copy-Item -Recurse -Force ".\adapters\skill\*" "$HOME\.claude\skills\humanize-russian-business-text\"
```

macOS / Linux:

```bash
git clone https://github.com/ValentinAvramko/editorial-skill-for-natural-russian-business-writing.git
cd editorial-skill-for-natural-russian-business-writing
mkdir -p ~/.claude/skills/humanize-russian-business-text
cp -R ./adapters/skill/* ~/.claude/skills/humanize-russian-business-text/
```

## Что должно получиться

Минимально для работы нужны:

- `SKILL.md`
- `adapter.yaml`
- `references/patterns.md`
- `references/examples.md`

Лишние platform-specific файлы внутри каталога можно не использовать: редакторская логика всё равно остаётся общей.

## Как вызывать

Простой вариант:

```text
/humanize-russian-business-text

Перепиши этот текст так, чтобы он звучал естественно и по-деловому. Не придумывай новые факты.

[ваш текст]
```

Более точный вариант:

```text
Это сопроводительное письмо.
Нужно убрать нейрояз, карьерные штампы и слишком гладкие формулировки, но сохранить спокойный профессиональный тон.
Если текст уже нормальный, правь минимально.
Верни только итоговый вариант.

[ваш текст]
```
