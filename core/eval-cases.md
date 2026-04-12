# Evaluation Cases

This file provides a compact evaluation set for checking whether the editorial skill behaves consistently across common Russian-language business writing tasks.

Use these cases to compare prompt revisions, model variants, or platform adapters.

## Evaluation Criteria

For each case, check:

1. Meaning preservation
2. No invented facts, motivation, or detail
3. Natural Russian business tone
4. Removal of AI phrasing, bureaucracy, and template language where relevant
5. No over-editing
6. No drift into casual, promotional, or synthetic tone

## Case 1: Cover Letter Template Language

### Input

Меня заинтересовала ваша вакансия, поскольку я обладаю высоким уровнем мотивации и уверен, что мой опыт будет полезен вашей команде. В течение своей карьеры я успешно решал сложные задачи и ориентирован на результат.

### Expected Behavior

- remove template career-service language
- keep the message concise
- do not invent concrete achievements
- make the text sound human and professional

## Case 2: Already Good Text, Minimal Edit

### Input

Добрый день. Посмотрел описание роли и думаю, что мой опыт может быть здесь полезен: я много работал на стыке продукта, аналитики и операционных процессов. Если будет уместно, буду рад коротко созвониться и рассказать подробнее.

### Expected Behavior

- edit minimally
- keep the structure mostly intact
- avoid making the text drier or more formal than needed

## Case 3: No Added Motivation

### Input

Я работал с похожими задачами в продуктовой команде и понимаю, как выстроить взаимодействие между разработкой, аналитикой и бизнесом.

### Expected Behavior

- keep the statement as-is or close to it
- do not add “this role is interesting to me” or similar motivation
- do not decorate the text

## Case 4: AI-Smooth Corporate Tone

### Input

Мой опыт позволяет эффективно адаптироваться к новым задачам, быстро погружаться в контекст и обеспечивать устойчивое качество результата в условиях высокой неопределенности.

### Expected Behavior

- reduce synthetic smoothness
- keep the meaning
- avoid replacing this with empty self-praise

## Case 5: Vacancy-Mirroring

### Input

Мне особенно близка возможность лидировать кросс-функциональные инициативы, драйвить трансформацию и усиливать value через системное взаимодействие со стейкхолдерами.

### Expected Behavior

- remove corporate jargon
- rephrase in normal Russian
- preserve relevance without mirroring vacancy language

## Case 6: Short Work Message

### Input

Коллеги, важно отметить, что в свою очередь нам необходимо проактивно синхронизироваться по следующему этапу работ.

### Expected Behavior

- make the text shorter and clearer
- keep it respectful
- avoid bureaucratic or synthetic phrasing

## Case 7: Project Description

### Input

В рамках проекта была обеспечена реализация единого процесса взаимодействия между продуктовыми и операционными командами, что позволило повысить прозрачность работы и эффективность принятия решений.

### Expected Behavior

- make the action and result explicit
- reduce bureaucracy
- keep the project description concrete

## Case 8: Case Description

### Input

Кейс продемонстрировал важность системного подхода и позволил сформировать основу для дальнейшего масштабирования практик взаимодействия между участниками процесса.

### Expected Behavior

- remove false importance
- replace empty abstraction with concrete meaning
- avoid over-inflating the case

## Case 9: Technical Requirement

### Input

Система должна обеспечивать возможность гибкой настройки уведомлений и поддерживать удобный механизм управления правами доступа с учетом специфики ролей пользователей.

### Expected Behavior

- preserve requirement precision
- rewrite abstract phrasing into clearer functional language
- do not weaken the requirement

## Case 10: Test Assignment

### Input

Необходимо реализовать решение, которое позволит продемонстрировать способность кандидата эффективно работать с данными, формировать выводы и визуализировать результаты в понятном формате.

### Expected Behavior

- simplify the wording
- preserve evaluation intent
- do not make the task vaguer

## Case 11: Acceptance Criteria

### Input

При изменении статуса заявки система должна обеспечивать автоматическую отправку уведомления пользователю и фиксировать факт отправки в журнале событий.

### Expected Behavior

- keep acceptance logic exact
- do not replace exact conditions with softer wording
- preserve sequence and system behavior

## Case 12: Architecture Constraint

### Input

Решение не должно требовать синхронного обмена между сервисами в критическом пути обработки запроса и должно сохранять работоспособность при временной недоступности очереди.

### Expected Behavior

- keep the architectural constraint precise
- avoid diluting the operational requirement
- preserve the negative constraint and resilience condition

## Case 13: Trade-Off Description

### Input

Мы отказались от более гибкой схемы конфигурации, потому что на этом этапе важнее было сократить количество точек отказа и упростить сопровождение решения.

### Expected Behavior

- keep the trade-off explicit
- do not make the choice sound more grand or strategic than it is
- preserve the practical reasoning

## Case 14: Over-Editing Trap

### Input

Добрый день. Я посмотрел описание роли и думаю, что мой опыт здесь может быть полезен: я много работал на стыке продукта, аналитики и операционных процессов. Если будет удобно, могу коротко рассказать о релевантных задачах.

### Expected Behavior

- avoid rewriting this into generic recruiter-template language
- keep the living tone
- make at most a light correction

## Failure Signals

The edit likely failed if:

- new achievements, motivation, or detail appeared
- the text became more polished but less human
- the text became drier and weaker than the source
- requirements or conditions became less precise
- the result sounds like a recruiter template or a generic AI answer
