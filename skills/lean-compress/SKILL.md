---
description: Safely compress a prompt, skill, rule, CLAUDE.md, or document without losing behavior.
argument-hint: <file path>
allowed-tools: Read, Write, Edit, Bash
---

Compress: $ARGUMENTS

1. Measure the original with `token_audit.py`.
2. Apply the rules in `references/prompt-compression.md`.
3. Write `<original>.lean<extension>`; never overwrite the source by default.
4. Compare structure and verify that every rule, constraint, warning, edge case, and meaningful example remains represented.
5. Re-measure and report actual before/after estimates plus intentional changes.

If semantic preservation cannot be verified, stop instead of claiming the compression is safe.
