---
description: Set lean-output mode (lite, standard, ultra, fast-build, off)
argument-hint: [lite|standard|ultra|fast-build|off]
---

The UserPromptSubmit hook persists the requested mode. Apply `lean-output` using that mode. If the mode is `fast-build`, also apply `lean-fast-build` to build requests.

Reply with one short confirmation. If the argument is invalid, use the configured default mode.
