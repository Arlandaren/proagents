---
title: "770 промптов для ИИ-разработчика: разбираем open-source библиотеку proagents"
subtitle: "Что внутри, как устроено и зачем это нужно каждому, кто пишет код с помощью LLM"
tags: [open-source, ai, llm, prompts, cursor, claude, архитектура, инструменты, разработка]
preview_description: >
  Открытый репозиторий proagents собрал 770+ системных промптов, разбитых
  по функциональным доменам: от правил безопасности и дизайн-систем до
  специализированных ролей (SRE, Solidity-разработчик, UX-исследователь)
  и пошаговых воркфлоу. Разбираемся, что там внутри и как правильно это использовать.
---

<!-- ПРЕВЬЮ-ИЗОБРАЖЕНИЕ: структура репозитория proagents в файловом менеджере или дереве папок, красивый dark-тон -->

## Зачем вообще библиотека промптов

С ростом использования Cursor, Claude Code и Windsurf у разработчиков появилась новая проблема: **как сделать так, чтобы ИИ всегда выдавал качественный результат**, а не только когда попросишь правильно?

Ответ — системные промпты. Они задают модели контекст ещё до вашего первого сообщения. Но написать хороший системный промпт — отдельная работа. Нужно знать, что туда включить, как структурировать требования, что важно для безопасности, что — для эстетики.

[proagents](https://github.com/Arlandaren/proagents) — это сборник таких промптов, написанных и проверенных заранее.

---

## Масштаб: что значит 770+

770 промптов — это не просто большое число. Это:

- **~150 правил** (rules/) — токены уровня кодовой гигиены и дизайн-системы
- **~350 персон** (personas/) — специализированные системные роли
- **~180 воркфлоу** (workflows/) — пошаговые инструкции для конкретных задач
- **~90 шаблонов** (templates/) — готовые структуры документов и ADR

Каждый промпт имеет метаданные: название, описание, теги. CLI ищет по этим данным.

---

## Блок 1: rules/ — фундамент качества

Правила делятся на два слоя.

### core/ — обязательные ограничения

Сюда входят вещи, которые должны быть в любом проекте:

- **code-hygiene** — никаких магических чисел, все константы именованные, нет закомментированного кода в продакшне
- **git-compliance** — Conventional Commits, атомарные коммиты, запрет на `fix` без контекста
- **error-handling** — try/catch только с конкретными типами ошибок, логирование через structured logger

### taste/ — дизайн и визуальный стиль

Это про эстетику кода и UI:

- **color-theory** — HSL вместо hex, семантические переменные цвета, темная тема из коробки
- **motion-design** — spring physics вместо `ease-in-out`, анимации только через CSS-переменные
- **layout-grids** — 8px-сетка, `clamp()` для адаптивной типографики, контейнеры с `max-width`

---

## Блок 2: personas/ — специализированные роли

Самый большой раздел. Persona — это системный промпт, который превращает модель в специалиста.

### engineering/

- **sre** — мыслит в SLO/SLI/error-budget, пишет runbooks, думает об observability
- **solidity-dev** — знает reentrancy, проверяет gas cost, форматирует по Solidity Style Guide
- **metal-renderer** — работает с Metal API, оптимизирует draw calls, знает pipeline-state objects
- **unity-multiplayer** — правила NetCode for GameObjects, authority models, lag compensation

### design/

- **ux-researcher** — строит user journey map, знает WCAG 2.2, думает accessibility-first
- **brand-guardian** — следит за visual identity, токенами дизайн-системы, tone of voice
- **motion-designer** — работает с принципами анимации Disney, spring physics, reduced motion

### operations/

- **code-auditor** — ищет security-issues, tech-debt, нарушения архитектурных контрактов
- **release-manager** — следует semantic versioning, пишет changelog, проверяет rollback-план
- **scrum-master** — управляет sprint planning, retrospective, Definition of Done

### business-strategy/

- **gtm-planner** — строит go-to-market стратегию, знает ICP, positioning, launch metrics
- **yc-coach** — мыслит в терминах traction, unit economics, investor narrative
- **proposal-strategist** — пишет RFP-ответы, win themes, executive summary

---

## Блок 3: workflows/ — пошаговые процессы

Если persona — это «кем быть», то workflow — это «что делать шаг за шагом».

### development/

- **tdd-cycle** — Red → Green → Refactor с конкретными чек-поинтами
- **deployment-guide** — последовательность шагов от staging до production с rollback
- **launch-checklist** — всё, что нужно проверить перед релизом

### qa-testing/

- **wcag-audit** — 50+ проверок доступности по WCAG 2.2 AA
- **responsive-validation** — тест на 320px, 768px, 1440px, 2560px
- **e2e-scenarios** — шаблоны сценариев для Playwright/Cypress

### security-compliance/

- **owasp-threat-model** — STRIDE-анализ по OWASP Top 10
- **dependabot-config** — правильная настройка автообновлений зависимостей
- **soc2-audit** — Evidence Collection Matrix для Type II аудита

---

## Блок 4: templates/ — готовые структуры

- **adr-template** — Architecture Decision Record в стандартном формате
- **spec-template** — функциональная спецификация с acceptance criteria
- **project-scaffold** — структура папок для нового проекта

---

## Как это всё соединяется

Типичный сценарий: новый проект на React + TypeScript.

```bash
# Базовые правила качества
python proagents.py install code-hygiene --cursor
python proagents.py install typescript-strict --cursor

# Дизайн-система
python proagents.py install ui-taste --cursor

# TDD-воркфлоу в CLAUDE.md
python proagents.py install tdd-cycle --stdout >> CLAUDE.md

# Перед деплоем
python proagents.py install launch-checklist --stdout
```

Каждый из этих промптов — не маркетинговая фраза, а конкретный список проверяемых правил, которые модель будет соблюдать.

---

## Открытый код, MIT-лицензия

Репозиторий агрегирует материалы из открытых источников. Все оригинальные авторства сохранены в `CREDITS.md`. Можно форкать, добавлять свои промпты, предлагать PR.

---

## Попробовать

🔗 **GitHub**: [github.com/Arlandaren/proagents](https://github.com/Arlandaren/proagents)

```bash
git clone https://github.com/Arlandaren/proagents
python proagents.py search <ваш стек>
```

Если разобрали структуру и стало интересно — ⭐ на GitHub и «Нравится» на Habr.  
Пишите в комментарии, какие домены хотели бы видеть расширенными — это реально влияет на приоритеты.
