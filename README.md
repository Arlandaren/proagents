# proagents

A curated repository of elite agentic system prompts, design guidelines, task workflows, and document templates consolidated from top-performing AI development projects. 

This repository strips out heavy environment-specific dependencies to focus exclusively on highly portable, instruction-rich markdown resources that immediately elevate the output quality of LLM engines.

---

## 📂 Repository Structure

The resources are organized into four functional directories to make them easy to navigate and load into your development environment:

```
proagents/
├── CREDITS.md                  # Detailed copyright & license attributions
├── rules/                      # System-wide rules and design constraints
│   ├── core/                   # Guidelines for code hygiene and context management
│   └── taste/                  # Rules to eliminate "AI slop", boring layouts, and Inter/Lila defaults
├── personas/                   # Domain-specific system prompts defining agent roles
│   ├── engineering/            # Software architects, language reviewers, and TDD guides
│   ├── design/                 # UI/UX designers, copywriters, and visual storytellers
│   ├── product/                # Product managers and YC startup advisors
│   ├── business-strategy/      # C-Level strategic mentors and analysts
│   ├── operations/             # Release managers, scrum leaders, and QA reviewers
│   └── specialized/            # Domain experts (legal, translation, finance, sales)
├── workflows/                  # Step-by-step task-oriented execution manuals
│   ├── development/            # Code auditing, TDD loops, and systematic debugging
│   ├── qa-testing/             # End-to-end user flows and accessibility audits
│   ├── security-compliance/    # Threat modeling, privacy, and regulatory audits
│   └── business-ops/           # Scenario war rooms, pitch prep, and market research
└── templates/                  # Reusable layouts, ADR structures, and presentation frameworks
```

---

## 🚀 How to Use

These files are standard markdown prompts. They are compatible with all modern AI-assisted IDEs and agents:

### 1. Cursor (.cursorrules)
Copy the contents of a rule (e.g., `rules/taste/taste-skill.md`) directly into your `.cursorrules` file at the root of your project, or reference them in the Cursor Settings under **Rules for AI**.

### 2. Claude Code (CLAUDE.md & System Prompts)
Integrate the workflow checklists or core rules into your project's `CLAUDE.md` to guide Claude's coding style, testing commands, and documentation requirements.

### 3. Trae / Zed / Windsurf
Import the role profiles in `personas/` into your custom instruction settings or system prompts.

---

## ⚖️ Licensing & Attribution

All content in this repository is gathered from open-source projects under permissive licenses (MIT and Apache 2.0). Original copyrights and attributions are fully preserved in [CREDITS.md](./CREDITS.md).
