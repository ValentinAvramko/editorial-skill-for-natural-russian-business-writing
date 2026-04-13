# Адаптер для Claude Code

Статус: active.

Этот каталог содержит рабочую упаковку редакторского стандарта под Claude Code.

Для переносимого и переиспользуемого адаптера здесь используется официальный формат Claude Code Skills: каталог skill-а с файлом `SKILL.md`.

- один основной файл инструкций `SKILL.md`;
- два локальных reference-файла для паттернов и примеров;
- общий слой оценки в `../../core/`.

## Что входит в адаптер

- `SKILL.md` — основной skill-файл Claude Code;
- `references/patterns.md` — локальный справочник нежелательных паттернов;
- `references/examples.md` — локальная калибровка тона и глубины правки;
- `adapter.yaml` — манифест адаптера.

## Рекомендуемая установка

Лучший практический вариант — установить адаптер как Claude Code skill.

### Вариант 1. Репозиторий уже у вас на компьютере

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills\humanize-russian-business-text" | Out-Null
Copy-Item -Recurse -Force ".\adapters\claude-code\*" "$HOME\.claude\skills\humanize-russian-business-text\"
```

macOS / Linux:

```bash
mkdir -p ~/.claude/skills/humanize-russian-business-text
cp -R ./adapters/claude-code/* ~/.claude/skills/humanize-russian-business-text/
```

После копирования перезапустите Claude Code, если skill не появился сразу.

### Вариант 2. Если хотите сначала клонировать репозиторий

Windows PowerShell:

```powershell
git clone https://github.com/ValentinAvramko/editorial-skill-for-natural-russian-business-writing.git
cd editorial-skill-for-natural-russian-business-writing
New-Item -ItemType Directory -Force "$HOME\.claude\skills\humanize-russian-business-text" | Out-Null
Copy-Item -Recurse -Force ".\adapters\claude-code\*" "$HOME\.claude\skills\humanize-russian-business-text\"
```

macOS / Linux:

```bash
git clone https://github.com/ValentinAvramko/editorial-skill-for-natural-russian-business-writing.git
cd editorial-skill-for-natural-russian-business-writing
mkdir -p ~/.claude/skills/humanize-russian-business-text
cp -R ./adapters/claude-code/* ~/.claude/skills/humanize-russian-business-text/
```

## Что должно получиться после установки

В каталоге, куда вы скопировали адаптер, должны лежать:

- `SKILL.md`
- `adapter.yaml`
- `references/patterns.md`
- `references/examples.md`

То есть итоговый путь будет таким:

- `~/.claude/skills/humanize-russian-business-text/SKILL.md`
- `~/.claude/skills/humanize-russian-business-text/references/patterns.md`
- `~/.claude/skills/humanize-russian-business-text/references/examples.md`

## Как использовать

После установки skill может:

- подхватываться автоматически по `description`;
- вызываться вручную по имени.

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

Если нужен комментарий к правкам:

```text
Перепиши текст.
Сначала дай итоговый вариант, потом коротко перечисли, какие паттерны ты убрал и что переформулировал.

[ваш текст]
```

## Когда всё же нужен `CLAUDE.md`

`CLAUDE.md` в Claude Code по-прежнему полезен, но для другого слоя:

- общие правила проекта;
- команды, workflow и архитектурный контекст;
- глобальные инструкции, которые должны применяться всегда.

Этот репозиторный адаптер решает другую задачу: переносимый специализированный редакторский skill.
