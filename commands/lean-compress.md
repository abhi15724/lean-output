---
description: Compress a prompt, skill, CLAUDE.md or document without losing rules
argument-hint: <file path>
allowed-tools: Read, Write, Edit, Bash
---

Compress: $ARGUMENTS

1. Baseline: `python ${CLAUDE_PLUGIN_ROOT}/skills/lean-output/scripts/token_audit.py $ARGUMENTS`.
2. Apply `${CLAUDE_PLUGIN_ROOT}/skills/lean-output/references/prompt-compression.md`.
3. Write to a new file with `.lean` before the extension. Never overwrite the original.
4. Re-run the audit on the new file.
5. Report in at most 5 lines: before/after estimate, and anything intentionally dropped. Confirm every rule, constraint, example and edge case survived.
