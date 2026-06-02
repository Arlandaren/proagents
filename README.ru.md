<p align="center">
  <img src="assets/banner.png" alt="proagents" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a> · <b>Русский</b> · <a href="README.zh.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/всего_промптов-794-6366f1?style=for-the-badge" alt="794">
  <img src="https://img.shields.io/badge/персон-232-8b5cf6?style=for-the-badge" alt="232">
  <img src="https://img.shields.io/badge/воркфлоу-521-a855f7?style=for-the-badge" alt="521">
  <img src="https://img.shields.io/badge/лицензия-MIT-22c55e?style=for-the-badge" alt="MIT">
</p>

---

**proagents** — кураторская библиотека из **794 профессиональных системных промптов, персон и пошаговых воркфлоу** для разработки с ИИ. Дистиллировано из 6 ведущих open-source фреймворков. Никаких зависимостей, никакой телеметрии — только чистый markdown.

---

## 📊 В цифрах

<table>
<tr>
<td align="center"><b>794</b><br><sub>Всего промптов</sub></td>
<td align="center"><b>232</b><br><sub>Персоны агентов</sub></td>
<td align="center"><b>521</b><br><sub>Воркфлоу-чеклисты</sub></td>
<td align="center"><b>41</b><br><sub>Правила и стиль</sub></td>
<td align="center"><b>11</b><br><sub>Покрытых доменов</sub></td>
<td align="center"><b>6</b><br><sub>Исходных фреймворков</sub></td>
</tr>
</table>

---

## ⚡ Зачем proagents?

| | Стандартный ИИ | proagents |
|---|---|---|
| **UI** | Серый Tailwind, системные шрифты | HSL-палитры, микроанимации, glassmorphism |
| **Безопасность** | Хардкод, пропущенные edge cases | Строгая валидация, типизированные ошибки |
| **Тестирование** | «Потом напишу тесты» | TDD с первой строки: red → green → refactor |
| **Производительность** | Лишние ре-рендеры | LCP-оптимизация, spring physics |

---

## 🚀 Быстрый старт

```bash
git clone https://github.com/Arlandaren/proagents.git
cd proagents

./proagents list                                          # список доменов
./proagents search react                                  # поиск по ключевому слову
./proagents install react-patterns --cursor              # → .cursor/rules/
./proagents install senior-fullstack --stdout >> CLAUDE.md
```

---

## 🗂️ Обзор доменов

### 🧑‍💻 Инженерные персоны — 126 агентов

| Агент | Что делает |
|---|---|
| `senior-fullstack` | Full-stack с жёсткими архитектурными принципами и code review |
| `react-build-resolver` | Диагностика и исправление Webpack/Vite сборок |
| `solidity-smart-contract-engineer` | EVM-контракты, газ-оптимизация, безопасность DeFi |
| `sre-site-reliability-engineer` | SLO, error budget, chaos engineering |
| `embedded-firmware-engineer` | Bare-metal/RTOS для ESP32, STM32, Nordic nRF |
| `godot-multiplayer-engineer` | MultiplayerAPI, ENet/WebRTC, RPCs для Godot 4 |
| `unity-architect` | ScriptableObjects, data-driven модульность, ECS |
| `macos-spatial-metal-engineer` | Swift + Metal, высокопроизводительный 3D, Vision Pro |
| `+ 118 других` | AI/ML, backend, DevOps, игровые движки, XR, блокчейн... |

### 🎨 Дизайн-персоны — 15 агентов

| Агент | Что делает |
|---|---|
| `design-ui-designer` | Дизайн-системы, библиотеки компонентов |
| `design-ux-architect` | CSS-архитектура, accessible-разметка |
| `design-brand-guardian` | Охрана голоса бренда и визуальной идентичности |
| `design-image-prompt-engineer` | Точные промпты для Midjourney, DALL·E, SD |
| `+ 11 других` | Motion-дизайнеры, инклюзивные визуалы, UX-исследователи... |

### ⚙️ Операционные персоны — 33 агента

| Агент | Что делает |
|---|---|
| `code-reviewer` | Code review с акцентом на корректность и безопасность |
| `react-reviewer` | React-паттерны, хуки, производительность рендера |
| `typescript-reviewer` | Строгая типизация, interface-контракты |
| `database-reviewer` | Схема БД, индексы, детекция N+1 |
| `+ 29 других` | Go, Python, Java, C#, C++ ревьюеры, PM-роли... |

### 💼 Бизнес-стратегия — 14 агентов

| Агент | Что делает |
|---|---|
| `chief-of-staff` | Фильтрация шума, управление процессами для руководителей |
| `executive-brief` | C-suite саммари по McKinsey SCQA + BCG Pyramid |
| `feedback-synthesizer` | Превращает обратную связь в приоритеты продукта |
| `government-digital-presales-consultant` | ToG-пресейл, интерпретация политик, тендерные документы |
| `+ 10 других` | GTM-планировщики, трендовые исследователи, стратеги... |

### 🔬 Специализированные — 44 агента

Legal tech, академия, финансы, XR, и другие узкие ниши.

---

## 📋 Воркфлоу-чеклисты — 521 total

### 🛠️ Разработка — 363 воркфлоу
`tdd-workflow` · `react-patterns` · `production-deployment` · `launch-strategy` · `stripe-integration-expert` · `liquid-glass-design` · `motion-advanced`

### 🔒 Безопасность & Комплаенс — 64 воркфлоу
`owasp-threat-modeling` · `soc2-compliance` · `gdpr-privacy` · `ai-security` · `threat-detection`

### 🧪 QA & Тестирование — 32 воркфлоу
`react-testing` · `browser-qa-testing` · `ab-test-setup` · `accessibility` · `api-test-suite-builder`

### 📊 Бизнес-операции — 62 воркфлоу
`github-ops` · `analytics` · `board-deck-builder` · `research` · `senior-secops`

---

## 🎨 Правила и стиль — 41 файл

`rules/taste/` устраняет визуальную посредственность:
- `animate` — Spring physics, покадровая анимация
- `brand` — HSL-теория цвета, кастомные шрифтовые стеки
- `liquid-glass` — Glassmorphism с правильными значениями backdrop-filter
- `overdrive` — Максимальная визуальная плотность для премиального результата

`rules/core/` — Нулевая толерантность: никаких магических значений, никаких секретов в коде.

---

## ⚙️ Интеграция с IDE

```bash
# Cursor
./proagents install react-patterns --cursor

# Claude Code
./proagents install code-reviewer --stdout >> CLAUDE.md

# Windsurf / Zed / Trae
./proagents install ux-architect --stdout
```

---

## ⚖️ Лицензия

Собрано из 6 open-source фреймворков под MIT и Apache 2.0.  
Оригинальные авторства сохранены в [CREDITS.md](./CREDITS.md).  
[MIT License](LICENSE) © 2026 Arlandaren
