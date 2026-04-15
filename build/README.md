# Руководство по сборке адаптеров

Этот каталог описывает служебный слой репозитория: как один редакторский стандарт из `core/` собирается в два готовых deliverable-пакета в `adapters/`.

Готовые артефакты лежат в:

- `adapters/skill/` для агентных сред и portable skills;
- `adapters/prompt/` для обычных чатов, проектов и Gems.

Служебные файлы сборки лежат в:

- [`build/adapter-contract.md`](./adapter-contract.md)
- [`build/sync-matrix.md`](./sync-matrix.md)
- [`build/manifests/`](./manifests/)
- [`build/template/`](./template/)
- [`test/smoke-checklist.md`](../test/smoke-checklist.md)

## Источник правды

Единственный источник правды для редакторского поведения находится в `core/`.

Сюда входят:

- `core/prompt-spec.md`
- `core/patterns.md`
- `core/examples.md`
- `core/eval-cases.md`
- `core/eval-rubric.md`

Если любой адаптер расходится с `core/` в редакторской логике, ограничениях, workflow или целевом тоне, приоритет всегда у `core/`.

## Какие пакеты собираются сейчас

### `adapters/skill/`

Этот адаптер даёт один переносимый `SKILL.md` для agent skills.

Он предназначен для:

- Codex;
- Claude Code;
- других сред, которые умеют работать с portable skills того же типа.

Внутри него:

- `SKILL.md` как единый entrypoint;
- `references/` как локальные runtime-справочники;
- `agents/openai.yaml` как metadata для Codex/OpenAI.

### `adapters/prompt/`

Этот адаптер даёт prompt-пакет для двух сценариев:

- quick chat в обычном диалоге;
- file-backed использование в ChatGPT Projects, GPTs, Gemini Gems и похожих форматах.

Внутри него:

- `humanize-russian-business-text.prompt.md` как самодостаточный quick-chat entrypoint;
- `humanize-russian-business-text.instructions.md` как тонкий instructions-слой, который вызывает основной prompt-файл;
- `humanize-russian-business-text.patterns.md` и `humanize-russian-business-text.examples.md` как плоский reference-слой.

## Что адаптеры могут менять

Адаптеры могут менять только слой доставки:

- metadata и front matter;
- platform-specific config;
- правила обращения к локальным reference-файлам;
- файловую структуру, нужную конкретному способу доставки;
- разделение одного prompt-слоя на основной prompt и settings-инструкции, если редакторская политика при этом не меняется и не дублируется вторым entrypoint-ом.

Это изменения упаковки, а не редакторской политики.

## Что адаптеры не могут менять

Адаптеры не могут:

- менять редакторский стандарт;
- смягчать жёсткие ограничения;
- перестраивать workflow;
- менять целевой тон;
- вводить новое допустимое поведение;
- заменять общий слой оценки своим локальным.

Важно: `SKILL.md` и prompt deliverable-файлы не являются независимыми авторскими документами. Они считаются производными deliverable-артефактами от `core/prompt-spec.md`.

## Политика справочных файлов

Локальные reference-файлы могут быть:

- прямыми копиями файлов из `core/`;
- сжатыми версиями, если смысл не меняется;
- перегруппированными версиями того же материала.

Но они не должны вводить другой редакторский стандарт.

Файлы оценки работают иначе:

- `core/eval-cases.md` остаётся общим;
- `core/eval-rubric.md` остаётся общей рубрикой.

Не копируйте evaluation-файлы в адаптеры без явной рабочей причины.

## Правило обновления

Если меняется редакторская политика, сначала обновляйте `core/`.

После этого проверьте, нужно ли синхронизировать:

1. `adapters/skill/SKILL.md`;
2. `adapters/prompt/humanize-russian-business-text.prompt.md`;
3. `adapters/prompt/humanize-russian-business-text.instructions.md`;
4. prompt reference-файлы;
5. пользовательские инструкции в `README.md`;
6. platform-specific config.

Не начинайте с правки адаптера, если изменение по сути редакторское.

Рабочий процесс синхронизации описан в [`build/sync-matrix.md`](./sync-matrix.md).
Этот файл остаётся обзором архитектуры адаптеров и границ между `core/` и deliverable-слоями.

## Автосборка производных файлов

Чтобы уменьшить риск drift между `core/` и deliverable-слоями, используйте вспомогательный скрипт:

```bash
python build/build_adapters.py sync
```

Он пересобирает:

- `adapters/skill/SKILL.md`;
- prompt entrypoint-ы в `adapters/prompt/`;
- prompt reference-файлы.

Для быстрой проверки без записи используйте:

```bash
python build/build_adapters.py check
```

Этот скрипт не заменяет review и eval, но закрывает механическую часть синхронизации, где чаще всего появляется случайный drift.

## Практический чеклист синхронизации

1. Понять, затрагивает ли изменение редакторское поведение, паттерны, примеры или оценку.
2. Если изменение редакторское, сначала обновить `core/`.
3. Проверить манифесты `build/manifests/skill.yaml` и `build/manifests/prompt.yaml`.
4. Обновить только те deliverable-файлы, которые реально зависят от изменённого источника.
5. Проверить, что `SKILL.md` и prompt deliverable-файлы по-прежнему не расходятся с `core/prompt-spec.md`.
   Для `instructions.md` это означает не дублировать спецификацию, а корректно требовать основной prompt-файл.
6. При значимом изменении поведения перепроверить результат на `core/eval-cases.md` и `core/eval-rubric.md`.

## Целевая структура

```text
build/
|-- README.md
|-- adapter-contract.md
|-- sync-matrix.md
|-- build_adapters.py
|-- manifests/
|   |-- skill.yaml
|   `-- prompt.yaml
`-- template/
    |-- README.md
    `-- adapter.yaml

adapters/
|-- skill/
|   |-- SKILL.md
|   |-- agents/
|   |   `-- openai.yaml
|   `-- references/
|       |-- patterns.md
|       `-- examples.md
`-- prompt/
    |-- humanize-russian-business-text.prompt.md
    |-- humanize-russian-business-text.instructions.md
    |-- humanize-russian-business-text.patterns.md
    `-- humanize-russian-business-text.examples.md
```

## Правило манифеста

У каждого активного адаптера должен быть манифест в `build/manifests/`.

Он отвечает на простые вопросы:

- какой deliverable производит адаптер;
- какой у него статус;
- от каких файлов в `core/` он зависит;
- какие локальные файлы критичны для работы;
- что должно быть проверено перед выпуском.

## Когда изменение относится к `core/`

Кладите изменение в `core/`, если оно влияет на:

- назначение и область применения;
- целевой тон;
- жёсткие ограничения;
- допустимое и недопустимое поведение;
- жанровые ориентиры;
- рабочий процесс;
- правило выдачи;
- таксономию паттернов;
- философию примеров;
- ожидания от оценки.

## Когда изменение относится к адаптеру

Кладите изменение в адаптер, если оно влияет на:

- упаковку под skill или prompt;
- platform-specific metadata;
- пользовательскую инструкцию в `README.md`;
- локальные правила загрузки reference-файлов;
- разделение quick-chat и settings-инструкций;
- platform-specific config.

## Текущее правило репозитория

В этом репозитории `core/` определяет редакторский стандарт, `build/` обслуживает сборку, а `adapters/` поставляет два готовых артефакта доставки: `skill` и `prompt`.
