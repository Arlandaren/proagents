<p align="center">
  <img src="assets/banner.png" alt="proagents banner" width="100%">
</p>

<p align="center">
  <b>English</b> | <a href="README.ru.md">Русский</a> | <a href="README.zh.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT%20%2F%20Apache%202.0-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Prompts-770%2B-violet" alt="Total Prompts">
  <img src="https://img.shields.io/badge/IDE--Ready-Cursor%20%7C%20Claude%20Code%20%7C%20Zed-success" alt="IDE Ready">
</p>

---

**proagents** is a curated, prefix-free library of **770+ professional system prompts and task workflows** for AI-assisted development (Cursor, Claude Code, Windsurf, Zed, and custom LLM agents). Meticulously structured into functional domains, this library is built to replace generic, low-quality LLM generations ("AI slop") with production-grade engineering, visual excellence, and strict compliance.

---

## ⚡ The "Aha!" Moment: Standard LLM vs. proagents

Most LLMs write generic, functional code that looks like a basic tutorial. **proagents** forces the model to act as a senior specialist with strict rules.

| Metric / Aspect | Standard AI Output ❌ | proagents Enhanced Output |
| :--- | :--- | :--- |
| **UI Aesthetics** | Generic blue/gray Tailwind buttons, raw layout, standard boring fonts. | Curated HSL palettes, smooth micro-animations, glassmorphism, modern custom typography. |
| **Code Safety** | Hardcoded secrets, missing error states, skipped edge cases. | Zero hardcoding, strict validation rules, robust try-catch with specific errors. |
| **Logic & Testing** | "Write the code first, maybe test it later." | Injected TDD cycles, clean folder separation, explicit interface contracts. |
| **Aero/Performance** | Heavy re-renders, unoptimized media assets. | Precise DOM operations, spring physics, LCP optimizations. |

---

## 🛠️ Interactive Workspace CLI

Instead of manually browsing through hundreds of files, use the zero-dependency CLI manager `proagents.py` to search and install rules straight into your workspace.

```bash
# 1. Search for a domain or technology (e.g. React)
python proagents.py search react

# 2. Get info and metadata on a specific rule
python proagents.py install react-patterns --info

# 3. Install it directly into Cursor rules configuration
python proagents.py install react-patterns --cursor

# 4. Or output it to stdout to append to CLAUDE.md
python proagents.py install production-deployment --stdout >> CLAUDE.md
```

---

## 📂 Registry Taxonomy

The library is organized into four main functional blocks to prevent project bloat:

```
proagents/
├── proagents.py                # Zero-dependency CLI manager
├── rules/                      # Global constraints & styling tokens
│   ├── core/                   # Code hygiene, git compliance, error handling
│   └── taste/                  # HSL color theory, custom motion, and layout grids
├── personas/                   # System instructions for specialized roles
│   ├── engineering/            # Metal renderer, Unity multiplayer, Solidity dev, SRE
│   ├── design/                 # UX researcher, brand guardian, motion designer
│   ├── operations/             # Code auditor, release manager, scrum master
│   ├── business-strategy/      # GTM planner, proposal strategist, YC coach
│   └── specialized/            # Legal billing, translation, finance trackers
├── workflows/                  # Step-by-step execution checklists
│   ├── development/            # TDD cycles, deployment guides, launch routines
│   ├── qa-testing/             # WCAG audits, responsive validation, end-to-end flows
│   ├── security-compliance/    # OWASP threat modeling, Dependabot config, SOC2 audits
│   └── business-ops/           # GitHub issue triage, operations reports
└── templates/                  # Reusable layouts, specs, and ADR structures
```

---

## ⚙️ How to Integrate

### 🎯 Cursor
Install any pattern directly to the root of your project:
```bash
python proagents.py install react-patterns --cursor
```
This generates a `.cursorrules` file containing exact instructions for Cursor.

### 🤖 Claude Code
Load a specific persona or release checklist directly into your project's `CLAUDE.md`:
```bash
python proagents.py install launch-strategy --stdout >> CLAUDE.md
```

### 💻 Zed / Windsurf / Trae
View any prompt and paste it into your editor's system instruction preferences:
```bash
python proagents.py install ux-architect --stdout
```

---

## ⚖️ License & Credits

Consolidated from open-source repositories under MIT and Apache 2.0. Original copyrights are fully preserved in [CREDITS.md](./CREDITS.md).
Licensed under the [MIT License](LICENSE) © 2026 Arlandaren.
