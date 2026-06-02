---
title: "Как я настраиваю Cursor и Claude Code за 3 команды — и что из этого получается"
subtitle: "Практический гайд по proagents CLI: поиск, установка, интеграция в любой редактор"
tags: [cursor, claude-code, ai, llm, prompts, cli, инструменты, продуктивность, open-source]
preview_description: >
  Не теория — только команды. Показываю, как с помощью одного Python-скрипта
  без зависимостей подключить библиотеку из 770+ профессиональных промптов
  к Cursor, Claude Code, Zed и Windsurf. Три команды — и ваш ИИ-помощник
  начинает писать код, как будто его сделал сеньор с десятилетним опытом.
---

<!-- ПРЕВЬЮ-ИЗОБРАЖЕНИЕ: терминал с командами proagents.py search + install, рядом открытый Cursor с .cursorrules -->

## Проблема, которую я решал

У меня в команде несколько разработчиков. Каждый настраивал Cursor по-своему: кто-то вообще без системного промпта, кто-то с куцей инструкцией на три строки. Код был разный — не по логике, а по качеству оформления, обработке ошибок, стилю.

Хотелось единый стандарт, который легко обновлять и который не надо держать в голове.

Нашёл [proagents](https://github.com/Arlandaren/proagents).

---

## Что это такое за 30 секунд

**proagents** — GitHub-репозиторий с **770+ системными промптами** для LLM-ассистентов. Они покрывают:

- правила кода (безопасность, стиль, гигиена)
- дизайн-системы (цвет, типографика, анимации)
- специализированные роли (SRE, UX-исследователь, Solidity-разработчик)
- воркфлоу (TDD, деплой, OWASP, WCAG-аудит)

Всё управляется через один скрипт `proagents.py` — никаких `npm install`, никаких виртуальных сред.

---

## Установка

```bash
git clone https://github.com/Arlandaren/proagents
cd proagents
```

Готово. Дальше только Python 3.8+, который уже есть на любой машине.

---

## Команда 1: поиск нужного промпта

```bash
python proagents.py search react
```

Вывод примерно такой:

```
Found 12 results for "react":
  react-patterns     → rules/core/react-patterns.md
  react-performance  → rules/taste/react-performance.md
  frontend-dev       → personas/engineering/frontend-dev.md
  ...
```

Можно искать по технологии (`typescript`, `docker`, `solidity`), по роли (`sre`, `ux`, `security`) или по задаче (`tdd`, `deployment`, `audit`).

---

## Команда 2: посмотреть что внутри

```bash
python proagents.py install react-patterns --info
```

Выведет метаданные и превью содержимого промпта — чтобы понять, подходит ли он вам, до установки.

---

## Команда 3: установить в редактор

### Cursor

```bash
python proagents.py install react-patterns --cursor
```

Скрипт создаёт (или дополняет) `.cursorrules` в корне проекта. С этого момента Cursor читает ваши правила перед каждым ответом.

Можно установить сразу несколько:

```bash
python proagents.py install react-patterns --cursor
python proagents.py install ui-taste --cursor
python proagents.py install security-hardening --cursor
```

### Claude Code

```bash
python proagents.py install production-deployment --stdout >> CLAUDE.md
```

Воркфлоу добавляется в `CLAUDE.md` и применяется к каждому разговору с Claude Code в этом проекте.

### Zed / Windsurf / Trae

```bash
python proagents.py install ux-architect --stdout
```

Выводит промпт в stdout — копируете и вставляете в поле системных инструкций вашего редактора.

---

## Реальный пример из моей работы

Задача: покрыть React-проект базовыми правилами качества.

```bash
# Стиль и дизайн
python proagents.py install ui-taste --cursor

# Безопасность и гигиена кода
python proagents.py install security-hardening --cursor

# TypeScript-стандарты
python proagents.py install typescript-strict --cursor
```

После этого Cursor:
- перестал предлагать `any` в TypeScript
- начал сам добавлять `aria-label` к интерактивным элементам
- прекратил хардкодить строки конфигурации

Три команды, пять минут работы. Разница — ощутимая.

---

## Структура репозитория для навигации

```
proagents/
├── rules/
│   ├── core/        ← гигиена кода, git, обработка ошибок
│   └── taste/       ← цвет, анимации, типографика
├── personas/
│   ├── engineering/ ← SRE, Solidity, Metal-renderer
│   ├── design/      ← UX-исследователь, бренд-гардиан
│   └── ...
├── workflows/
│   ├── development/ ← TDD, деплой, релиз-чек-листы
│   ├── qa-testing/  ← WCAG, responsive, e2e
│   └── security-compliance/ ← OWASP, SOC2, Dependabot
└── templates/       ← ADR, спецификации, структуры
```

---

## Для командной работы

Лучший вариант — добавить `.cursorrules` в git. Тогда все в команде автоматически работают с одними и теми же правилами.

```bash
# Установить правила
python proagents.py install react-patterns --cursor

# Закоммитить
git add .cursorrules
git commit -m "chore: add proagents rules for react"
```

Единый стандарт без митингов и внутренних вики.

---

## Ссылка

🔗 [github.com/Arlandaren/proagents](https://github.com/Arlandaren/proagents)

Если инструмент полезен — ⭐ на GitHub и «Нравится» на Habr помогают проекту попасть к большему числу разработчиков.

Если возникли вопросы по конкретным правилам или интеграции — пишите в комментарии.
