<div align="center">

<img src="assets/lean-output.svg" alt="Lean Output" width="110"/>

# Lean Output

### ⚡ Less Noise. More Useful Work.

**A professional efficiency toolkit for Claude Code — designed to reduce unnecessary context, sharpen responses, and accelerate software delivery without sacrificing quality.**

<br/>

[![Version](https://img.shields.io/github/package-json/v/abhi15724/lean-output?style=for-the-badge&label=version&color=7c3aed)](https://github.com/abhi15724/lean-output)
[![Stars](https://img.shields.io/github/stars/abhi15724/lean-output?style=for-the-badge&color=f59e0b)](https://github.com/abhi15724/lean-output/stargazers)
[![License](https://img.shields.io/github/license/abhi15724/lean-output?style=for-the-badge&color=2563eb)](https://github.com/abhi15724/lean-output/blob/main/LICENSE)
[![Tests](https://img.shields.io/badge/tests-5%2F5%20passing-16a34a?style=for-the-badge)](https://github.com/abhi15724/lean-output/tree/main/tests)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-d97706?style=for-the-badge)](https://docs.anthropic.com/en/docs/claude-code)

</div>

---

## ✨ Why Lean Output?

AI coding assistants can waste context on repetition, verbose narration, duplicated instructions, and unnecessary clarification.

**Lean Output applies disciplined compression instead:**

> **Optimize for useful work per token — not minimum words.**

It keeps the important things: **correctness, security, edge cases, validation, accessibility, and user-requested detail.**

---

## 🚀 What You Get

<table>
<tr>
<td width="50%">

### 🎯 Lean Modes
Choose the response behavior that fits the task.

- `lite` — remove filler
- `standard` — concise + complete
- `ultra` — maximum useful brevity
- `fast-build` — optimized software delivery
- `off` — disable lean guidance

</td>
<td width="50%">

### ⚡ Fast Build
Ship a working vertical slice before expanding scope.

- Batch independent changes
- Reduce rework
- Keep quality gates
- Run smoke checks
- Create resumable handoffs

</td>
</tr>
<tr>
<td>

### 🔍 Context Audit
Find expensive always-loaded instructions and prioritize the highest-value reductions.

### 🗜️ Safe Compression
Compress prompts, skills, rules, and docs while preserving behavioral requirements.

</td>
<td>

### 📊 Usage & Review
Measure local transcript volume and identify removable verbosity without inventing savings.

### 🛡️ Quality First
Token efficiency never overrides correctness, security, validation, or requested depth.

</td>
</tr>
</table>

---

## 🧠 The Lean Ladder

| Mode | Best for | Behavior |
|:---|:---|:---|
| 🟢 **Lite** | Everyday work | Less filler and repetition |
| 🔵 **Standard** | Default | Answer first, tight structure |
| 🟣 **Ultra** | Token-sensitive tasks | Result-first, very terse |
| 🟠 **Fast Build** | Coding | Fast vertical-slice implementation |
| ⚪ **Off** | Full responses | Normal response behavior |

> 💡 Say **“full detail”** or **“explain step by step”** to override brevity for a turn.

---

## 📦 Commands

| Command | What it does |
|---|---|
| `/lean` | Enable the configured default mode |
| `/lean lite` | Enable Lite |
| `/lean standard` | Enable Standard |
| `/lean ultra` | Enable Ultra |
| `/lean fast-build` | Enable Fast Build |
| `/lean off` | Disable Lean Output |
| `/lean-fast-build <idea>` | Start a fast software build |
| `/lean-audit` | Audit always-loaded context |
| `/lean-compress <file>` | Safely compress a file |
| `/lean-review [file]` | Review unnecessary verbosity |
| `/lean-gain [--last N]` | Report local transcript usage |
| `/lean-help` | Show the command reference |

---

## 🛠️ Installation

### Claude Code

Install the plugin from your local clone:

```bash
git clone https://github.com/abhi15724/lean-output.git
cd lean-output
```

Then add the plugin using your preferred Claude Code plugin workflow.

### Verify

```bash
python3 -m unittest discover -s tests -v
```

Expected:

```text
Ran 5 tests
OK
```

---

## ⚙️ Configuration

Lean Output resolves its default mode in this order:

**1. Environment variable**

```bash
export LEAN_DEFAULT_MODE=ultra
```

**2. User configuration**

```text
~/.config/lean-output/config.json
```

Example:

```json
{
  "defaultMode": "standard",
  "language": "auto",
  "maxClarifyingQuestions": 1,
  "showUsageEstimates": false,
  "fastBuild": {
    "writeHandoff": true,
    "runSmokeCheck": true
  }
}
```

**3. Fallback**

```text
standard
```

---

## 📐 Design Principles

### 01 — Efficient, not careless
Never remove a security warning, constraint, edge case, validation step, or requested detail merely to save tokens.

### 02 — Measure, don’t guess
The included audit tools provide **heuristic estimates**, not tokenizer-exact counts.

### 03 — Build vertically
Fast Build gets the smallest end-to-end path working before expanding scope.

### 04 — Reduce rework
Batch independent changes, verify meaningful work, and leave a handoff when work spans turns.

### 05 — Keep quality visible
A shorter answer is only better when it remains accurate, actionable, and complete enough for the task.

---

## 🧰 Tooling

```text
lean-output/
├── .claude-plugin/     Plugin + marketplace metadata
├── commands/           Slash commands
├── config/             Editable defaults
├── hooks/              Persistent mode handling
├── rules/              Core rules
├── agents/             Specialized helpers
├── benchmarks/         Benchmarking notes
├── skills/             Lean workflows
├── scripts/            Repository utilities
├── tests/              Regression tests
└── assets/             Project branding
```

---

## 📊 Measurement

Audit a file:

```bash
python3 skills/lean-output/scripts/token_audit.py README.md
```

Inspect local transcript volume:

```bash
python3 skills/lean-output/scripts/usage_report.py --last 10
```

Review a file for unnecessary verbosity:

```text
/lean-review path/to/file.md
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a focused branch.
3. Make one coherent change.
4. Run the regression suite.
5. Open a pull request with the motivation and verification result.

Please keep contributions aligned with the core principle:

**Less noise. More useful work. No shortcuts on quality.**

---

## 📄 License

Distributed under the repository’s [LICENSE](LICENSE).

---

<div align="center">

### Built for efficient AI-assisted development.

**Lean Output v2.0.0**

[⭐ Star the project](https://github.com/abhi15724/lean-output) · [🐛 Report an issue](https://github.com/abhi15724/lean-output/issues) · [💡 Request a feature](https://github.com/abhi15724/lean-output/issues)

</div>