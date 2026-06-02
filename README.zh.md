<p align="center">
  <img src="assets/banner.png" alt="proagents banner" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README.ru.md">Русский</a> | <b>简体中文</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT%20%2F%20Apache%202.0-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Prompts-770%2B-violet" alt="Total Prompts">
  <img src="https://img.shields.io/badge/IDE--Ready-Cursor%20%7C%20Claude%20Code%20%7C%20Zed-success" alt="IDE Ready">
</p>

---

**proagents** 是一个精简且无前缀的提示词库，包含 **770+ 个专业的系统提示词（System Prompts）和任务工作流（Workflows）**，适用于 AI 辅助开发（Cursor, Claude Code, Windsurf, Zed 和自定义 LLM 智能体）。本仓库资源按照功能领域进行组织，旨在消除 AI 编写代码时的同质化与低质量（"AI slop"），为您的开发环境注入生产级别的工程实践、视觉美感以及合规检查。

---

## ⚡ 惊叹时刻 (Aha! Moment)：普通 AI 输出 vs. proagents

大多数 LLM 默认会编写非常通用的、教学水平的代码。**proagents** 强制模型以具有严格约束的高级专家身份进行输出。

| 维度 / 指标 | 标准 AI 输出 ❌ | proagents 增强版输出 |
| :--- | :--- | :--- |
| **UI 视觉美感** | 默认的灰色/蓝色 Tailwind 按钮、基础布局、浏览器默认字体。 | 精心调配的 HSL 配色、流畅的微动画、磨砂玻璃效果（glassmorphism）以及现代自定义字体。 |
| **代码安全性** | 硬编码密钥、缺失的错误状态处理、忽略边界情况。 | 零硬编码、严格的输入验证、带有具体错误类型的健壮 try-catch 结构。 |
| **逻辑与测试** | “先写代码，以后有空再写测试。” | 强制引入 TDD 测试循环、清晰的目录结构分离、显式的接口契约。 |
| **性能表现** | 频繁的重复渲染、未优化的多媒体静态资源。 | 精确的 DOM 操作、弹簧物理动画（spring physics）、LCP 指标优化。 |

---

## 🛠️ 交互式终端工具 CLI

无需手动翻阅数百个 Markdown 文件，使用无依赖的 Python CLI 工具 `proagents.py` 即可轻松搜索和安装规则到您的本地项目中。

```bash
# 1. 搜索特定技术或领域的提示词（例如 React）
python proagents.py search react

# 2. 查看特定规则的元数据和描述信息
python proagents.py install react-patterns --info

# 3. 将规则直接安装到 Cursor 配置文件中 (.cursorrules)
python proagents.py install react-patterns --cursor

# 4. 或者将内容输出到终端以追加到 CLAUDE.md 中
python proagents.py install production-deployment --stdout >> CLAUDE.md
```

---

## 📂 仓库结构

所有资源划分为四个清晰的功能目录：

```
proagents/
├── proagents.py                # 无依赖的 CLI 管理工具
├── rules/                      # 全局约束与样式规范
│   ├── core/                   # 代码健康、Git 规范、错误处理
│   └── taste/                  # HSL 色彩理论、自定义动态交互与布局网格
├── personas/                   # 特定角色的系统指令
│   ├── engineering/            # Metal 渲染专家、Unity 多人游戏工程师、Solidity 开发者、SRE
│   ├── design/                 # UX 研究员、品牌卫士、动效设计师
│   ├── operations/             # 代码审计师、发布经理、Scrum Master
│   ├── business-strategy/      # GTM 策划师、提案架构师、YC 创业教练
│   └── specialized/            # 垂直领域专家（法律账单、专业翻译、财务记账）
├── workflows/                  # 任务执行指南与检查清单
│   ├── development/            # TDD 循环、部署指南、发布检查清单
│   ├── qa-testing/             # WCAG 可访问性审计、响应式验证、端到端测试流程
│   ├── security-compliance/    # OWASP 威胁建模、Dependabot 配置、SOC2 审计
│   └── business-ops/           # GitHub Issue 分流与整理、运营报告
└── templates/                  # 可复用的框架、技术规范与 ADR 结构模板
```

---

## ⚙️ 如何集成

### 🎯 Cursor
直接将任意模式安装到项目根目录下：
```bash
python proagents.py install react-patterns --cursor
```
这会生成包含严格说明的 `.cursorrules` 文件。

### 🤖 Claude Code
将特定的发布检查清单或工作流直接加载到 `CLAUDE.md`：
```bash
python proagents.py install launch-strategy --stdout >> CLAUDE.md
```

### 💻 Zed / Windsurf / Trae
在终端中查看任意提示词，然后复制并粘贴到您的编辑器的系统提示词偏好设置中：
```bash
python proagents.py install ux-architect --stdout
```

---

## ⚖️ 许可与致谢

从 MIT 和 Apache 2.0 许可的开源项目整理而来。原作者的版权与署名信息均完整保留在 [CREDITS.md](./CREDITS.md) 中。
在 [MIT 许可证](LICENSE) 下发布 © 2026 Arlandaren。
