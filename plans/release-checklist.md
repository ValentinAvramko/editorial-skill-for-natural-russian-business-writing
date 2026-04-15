# Release-checklist

Этот файл нужен как короткий список финальных действий перед выпуском.

Он не заменяет `test/smoke-checklist.md`, а собирает в одном месте финальные действия по содержанию, проверке и публикации.

## Перед выпуском

- [ ] Убедиться, что `core/` содержит все канонические редакторские изменения.
- [ ] Запустить `python build/build_adapters.py check` и убедиться, что `SKILL.md`, prompt entrypoint-ы и локальные reference-файлы не ушли в drift.
- [ ] Просмотреть `README.md` и `build/README.md` и убедиться, что они соответствуют текущей структуре репозитория.
- [ ] Проверить `build/manifests/skill.yaml` и `build/manifests/prompt.yaml`.
- [ ] Проверить `adapters/skill/agents/openai.yaml`, если менялись skill metadata или способы вызова в Codex.
- [ ] Пройти [`test/smoke-checklist.md`](../test/smoke-checklist.md) для `skill` и `prompt`.

## Перед публикацией

- [ ] Проверить, что примеры в `README.md` соответствуют текущему поведению.
- [ ] При значимых изменениях поведения перепроверить результат на `core/eval-cases.md` и `core/eval-rubric.md`.
- [ ] Убедиться, что release-коммуникация не смешивает пользовательский и служебный слой.
