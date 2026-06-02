<p align="center">
  <img src="assets/banner.png" alt="proagents banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT%20%2F%20Apache%202.0-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Prompts-770%2B-violet" alt="Total Prompts">
  <img src="https://img.shields.io/badge/IDE--Ready-Cursor%20%7C%20Claude%20Code%20%7C%20Zed-success" alt="IDE Ready">
</p>

---

**proagents** is a clean, domain-organized library of **770+ professional system personas and execution workflows** for AI-assisted development. Consolidated from top-performing agent frameworks, it is built to eliminate generic LLM outputs ("AI slop") and inject rich, production-grade coding standards, visual aesthetics, and compliance checks directly into your workspace.

---

## ⚡ Highlights

* **Zero Hype, Pure Prompting**: No heavy packages, node wrappers, or telemetry scripts. Just high-quality, instruction-rich markdown.
* **CLI-Driven Setup**: An interactive, zero-dependency Python script to search and install rules into `.cursorrules` or `.claude/` in a single command.
* **Functional Domain Layout**: Sanitized file naming, free of vendor-specific prefixes (`ecc-`, `agency-`, etc.), organized strictly by domain.
* **Tuned for Visual Taste**: Includes 40+ dedicated rules for HSL tailored colors, premium typography, custom micro-animations, and glassmorphism, completely replacing default unstyled outputs.

---

## 🛠️ The proagents CLI Tool

We include `proagents.py`, a lightweight Python utility to manage prompts locally.

### Usage

```bash
# List all categories and counts of personas/workflows
python proagents.py list

# List all personas in engineering
python proagents.py list personas/engineering

# Search for any prompt containing a keyword (e.g. "react")
python proagents.py search react

# Install a workflow straight to your local .cursorrules file
python proagents.py install react-patterns --cursor

# Copy a persona to a custom file location
python proagents.py install ux-architect --target .claude/skills/ux-architect.md

# View description and metadata of a rule
python proagents.py install launch-strategy --info
```

---

## 📂 Repository Anatomy

The repository is structured into four main directories:

```
proagents/
├── proagents.py                # Zero-dependency CLI manager
├── rules/                      # System-wide constraints & guidelines
│   ├── core/                   # Code hygiene, git limits, and clean logic
│   └── taste/                  # Visual guidelines, color theory, & UI aesthetics
├── personas/                   # System instructions defining specific roles
│   ├── engineering/            # Smart contract engineers, game scripters, etc.
│   ├── design/                 # UX architects, brand guardians, motion artists
│   ├── operations/             # Release managers, code reviewers, scrum masters
│   ├── business-strategy/      # GTM planners, YC mentors, pitch evaluators
│   └── specialized/            # Domain experts (legal tech, finance, translators)
├── workflows/                  # Detailed execution checklists
│   ├── development/            # TDD loops, deployment, launch checklists
│   ├── qa-testing/             # WCAG accessibility audits, user flows
│   ├── security-compliance/    # OWASP threat modeling, SOC2 audits
│   └── business-ops/           # GitHub triage, operations, reporting
└── templates/                  # Reusable ADRs, templates, and specs
```

---

## 🎨 Domain & Agent Coverage

Here is the breakdown of the **770+ agents and checklists** included:

### 1. Rules & Visual Taste (`rules/`)
* **Core Rules**: Clean styling guidelines, explicit over implicit declarations, config schema limits.
* **Taste Rules**: Eliminates vanilla colors. Enforces Inter/Outfit/Roboto typography, smooth gradients, HSL tailored color schemes, frame-perfect micro-animations, and CSS layout grids.

### 2. Specialized Personas (`personas/`)
* **Engineering**: Includes native 3D rendering (`macos-spatial-metal-engineer`), specialized gaming engines (`godot-multiplayer-engineer`, `unity-architect`), Web3 smart contracts (`solidity-smart-contract-engineer`), and infrastructure (`sre-site-reliability-engineer`).
* **Design & UX**: Focuses on UI/UX excellence (`ui-designer`, `ux-researcher`), brand voice protection (`brand-guardian`), and animation specialists.
* **Operations & QA**: Practical roles for code audits (`code-reviewer`), task prioritization (`sprint-prioritizer`), and CI/CD triage.
* **Business Strategy**: Presales planners (`proposal-strategist`), target market analysts (`trend-researcher`), and growth engineers.

### 3. Systematic Workflows (`workflows/`)
* **Development Playbooks**: Comprehensive checklists for `launch-strategy`, TDD routines, local container deployment, and performance optimization.
* **Security & Compliance**: Outlines setups for OWASP audits, Dependabot security monitoring, HIPAA / SOC2 checks, and secret scanning.
* **QA & Testing**: Outlines WCAG accessibility audits, responsive design verification, and playwright-driven user flows.

---

## 🚀 IDE Integration Guide

### Cursor (`.cursorrules`)
To load a proagents prompt as a permanent instruction template for Cursor:
```bash
python proagents.py install react-patterns --cursor
```

### Claude Code (`CLAUDE.md`)
Append specific workflows to your `CLAUDE.md` to keep Claude Code aligned with testing and style constraints:
```bash
python proagents.py install launch-strategy --stdout >> CLAUDE.md
```

### Zed / Windsurf / Trae
Copy the contents of the relevant markdown file inside `personas/` or `workflows/` and paste them into the system prompt configuration or custom instructions settings under your editor configurations.

---

## ⚖️ License

Consolidated from permissive open-source repositories (MIT and Apache 2.0). Original copyrights and attributions are preserved in [CREDITS.md](./CREDITS.md).
