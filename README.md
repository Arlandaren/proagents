<p align="center">
  <img src="assets/banner.png" alt="proagents" width="100%">
</p>

<p align="center">
  <b>English</b> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/total_prompts-794-6366f1?style=for-the-badge" alt="794 prompts">
  <img src="https://img.shields.io/badge/personas-232-8b5cf6?style=for-the-badge" alt="232 personas">
  <img src="https://img.shields.io/badge/workflows-521-a855f7?style=for-the-badge" alt="521 workflows">
  <img src="https://img.shields.io/badge/license-MIT-22c55e?style=for-the-badge" alt="MIT">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Cursor-compatible-blue?style=flat-square" alt="Cursor">
  <img src="https://img.shields.io/badge/Claude_Code-compatible-orange?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/Windsurf-compatible-cyan?style=flat-square" alt="Windsurf">
  <img src="https://img.shields.io/badge/Zed-compatible-green?style=flat-square" alt="Zed">
  <img src="https://img.shields.io/badge/Gemini_CLI-compatible-yellow?style=flat-square" alt="Gemini CLI">
</p>

---

**proagents** is a curated, prefix-free library of **794 professional system prompts, agent personas, and task workflows** distilled from 6 leading open-source agent frameworks. No wrappers, no telemetry, no dependencies. Drop any file into your AI IDE and the model immediately operates as a senior specialist.

---

## 📊 By the Numbers

<table>
<tr>
<td align="center"><b>794</b><br><sub>Total prompts</sub></td>
<td align="center"><b>232</b><br><sub>Agent personas</sub></td>
<td align="center"><b>521</b><br><sub>Workflow checklists</sub></td>
<td align="center"><b>41</b><br><sub>Rules & taste tokens</sub></td>
<td align="center"><b>11</b><br><sub>Domains covered</sub></td>
<td align="center"><b>6</b><br><sub>Source frameworks</sub></td>
</tr>
</table>

---

## ⚡ Why proagents?

Most AI IDE prompts are written once, never maintained, and produce generic outputs. These were battle-tested across real production projects and distilled into a clean, domain-organized format. The difference is immediate:

| | Default AI | proagents |
|---|---|---|
| **UI Output** | Generic Tailwind, boring layout, system fonts | Curated HSL palettes, micro-animations, glassmorphism |
| **Code Safety** | Hardcoded values, missing edge cases | Zero magic strings, strict validation, typed errors |
| **Testing** | "I'll add tests later" | TDD first: red → green → refactor |
| **Security** | OWASP basics ignored | Threat modeling built into every review |
| **Performance** | Unoptimized, re-renders everywhere | LCP targets, spring physics, precise DOM ops |

---

## 🚀 Quick Start

```bash
git clone https://github.com/Arlandaren/proagents.git
cd proagents

# List all domains and counts
python proagents.py list

# Search by keyword
python proagents.py search react

# Install to Cursor (.cursorrules)
python proagents.py install react-patterns --cursor

# Install to Claude Code (CLAUDE.md)
python proagents.py install senior-fullstack --stdout >> CLAUDE.md

# Preview any prompt
python proagents.py install ux-architect --stdout
```

No pip installs. Works on Python 3.8+.

---

## 🗂️ Domain Overview

### 🧑‍💻 Engineering Personas — 126 agents

Deep specialists, not generic "act as a developer" prompts. Each has a defined personality, strict rules, and measurable output standards.

| Agent | What it does |
|---|---|
| `senior-fullstack` | Full-stack engineer with strict architectural opinions and code review standards |
| `react-build-resolver` | Diagnoses and fixes Webpack/Vite build failures in React/Next.js projects |
| `mobile-app-builder` | Native iOS/Android + React Native/Flutter specialist |
| `solidity-smart-contract-engineer` | EVM contracts, gas optimization, DeFi protocol security |
| `sre-site-reliability-engineer` | SLOs, error budgets, chaos engineering, toil reduction |
| `embedded-firmware-engineer` | Bare-metal / RTOS for ESP32, STM32, Nordic nRF |
| `godot-multiplayer-engineer` | MultiplayerAPI, ENet/WebRTC, RPCs for Godot 4 |
| `unity-architect` | ScriptableObjects, data-driven modularity, ECS/DOTS |
| `macos-spatial-metal-engineer` | Swift + Metal, high-performance 3D, Vision Pro |
| `lsp-index-engineer` | Language Server Protocol, semantic code intelligence |
| `+ 116 more` | AI/ML, backend, DevOps, game engines, XR, blockchain... |

### 🎨 Design Personas — 15 agents

| Agent | What it does |
|---|---|
| `design-ui-designer` | Visual design systems, component libraries, brand consistency |
| `design-ux-architect` | CSS architecture, accessible layouts, implementation guidance |
| `design-brand-guardian` | Brand voice, visual identity enforcement, positioning |
| `design-ux-researcher` | Usability testing, behavior analysis, actionable research |
| `design-image-prompt-engineer` | Expert prompts for Midjourney, DALL·E, Stable Diffusion |
| `design-inclusive-visuals-specialist` | Bias-free, culturally accurate AI imagery |
| `+ 9 more` | Motion designers, whimsy injectors, visual storytellers... |

### ⚙️ Operations Personas — 33 agents

| Agent | What it does |
|---|---|
| `code-reviewer` | Constructive review focused on correctness, security, and maintainability |
| `react-reviewer` | React-specific patterns, hooks discipline, render performance |
| `typescript-reviewer` | Strict type safety, interface contracts, inference quality |
| `codebase-onboarding-engineer` | Helps new devs understand unfamiliar repos from the source |
| `database-reviewer` | Schema design, index strategy, N+1 detection |
| `automation-governance-architect` | Audits automation value, risk, and maintainability |
| `+ 27 more` | Go, Python, Java, C#, C++ reviewers + PM roles... |

### 💼 Business Strategy — 14 agents

| Agent | What it does |
|---|---|
| `chief-of-staff` | Filters noise, owns processes, routes decisions for executives |
| `executive-brief` | C-suite summaries using McKinsey SCQA + BCG Pyramid |
| `feedback-synthesizer` | Turns raw user feedback into quantified product priorities |
| `behavioral-nudge-engine` | Behavioral psychology to maximize user motivation |
| `government-digital-presales-consultant` | ToG presales, policy interpretation, bid documents |
| `cross-border-ecommerce` | Amazon, Shopee, Lazada, AliExpress full-funnel ops |
| `+ 8 more` | GTM planners, trend researchers, proposal strategists... |

### 🔬 Specialized — 44 agents

Niche experts covering legal tech, academia, finance, spatial computing, and more.

| Agent | What it does |
|---|---|
| `legal-document-review` | Contract review, risk clause flagging, version comparison |
| `blockchain-security-auditor` | Smart contract vulnerability detection, audit reports |
| `academic-anthropologist` | Culturally coherent society design, kinship systems |
| `academic-psychologist` | Psychologically credible characters and interactions |
| `workflow-architect` | Maps every workflow path before a line of code is written |
| `mcp-builder` | Builds Model Context Protocol servers for AI agents |
| `+ 38 more` | Civil engineers, supply chain, HR, real estate, XR, finance... |

---

## 📋 Workflow Checklists — 521 total

### 🛠️ Development — 363 workflows

The largest domain. Complete execution checklists covering every phase of software delivery.

**Highlights:** `tdd-workflow` · `react-patterns` · `senior-fullstack` · `production-deployment` · `launch-strategy` · `stripe-integration-expert` · `liquid-glass-design` · `motion-advanced` · `nextjs-patterns` · `swift-actor-persistence` · `remote-mcp-server`

### 🔒 Security & Compliance — 64 workflows

`owasp-threat-modeling` · `soc2-compliance` · `gdpr-privacy` · `ai-security` · `threat-detection` · `security-review` · `blockchain-audit` · `dependency-auditor`

### 🧪 QA & Testing — 32 workflows

`react-testing` · `browser-qa-testing` · `ab-test-setup` · `accessibility` · `ai-regression-testing` · `api-test-suite-builder`

### 📊 Business Ops — 62 workflows

`github-ops` · `analytics` · `board-deck-builder` · `autonomous-loops` · `research` · `senior-secops`

---

## 🎨 Rules & Taste Tokens — 41 files

The `rules/` directory is the most impactful single folder. It shapes *how* the model generates, not just what it generates.

**`rules/taste/`** — Eliminates visual mediocrity:
- `animate` — Spring physics, frame-perfect motion, no CSS transitions
- `bolder` — Forces decisive type hierarchy, no weak grays
- `brand` — HSL-based color theory, custom font stacks
- `liquid-glass` — Glassmorphism with correct backdrop-filter values
- `motion-advanced` — Bezier curves, staggered reveals, scroll-triggered animations
- `overdrive` — Maximum visual density when you need premium impact

**`rules/core/`** — Zero-tolerance code hygiene: no magic values, no hardcoded secrets, no silent failures.

---

## ⚙️ IDE Integration

### Cursor
```bash
# Install a workflow as .cursorrules
python proagents.py install react-patterns --cursor

# Or reference specific rules in Cursor Settings → Rules for AI
cat rules/taste/animate.md
```

### Claude Code
```bash
# Append any persona to CLAUDE.md
python proagents.py install code-reviewer --stdout >> CLAUDE.md

# Load a taste rule for visual work
python proagents.py install brand --stdout >> CLAUDE.md
```

### Windsurf / Zed / Trae
```bash
# Output to stdout and paste into system instructions
python proagents.py install ux-architect --stdout
```

### Gemini CLI
```bash
# Install a skill file to ~/.gemini/extensions/
python proagents.py install senior-fullstack --target ~/.gemini/extensions/proagents/SKILL.md
```

---

## 🤝 Contributing

1. Fork the repo
2. Add your `.md` file in the appropriate `personas/` or `workflows/` domain
3. No YAML frontmatter required — clean markdown is enough
4. Open a PR

---

## ⚖️ License & Credits

Consolidated from 6 open-source frameworks under MIT and Apache 2.0 licenses.  
Original attributions preserved in [CREDITS.md](./CREDITS.md).  
[MIT License](LICENSE) © 2026 Arlandaren
