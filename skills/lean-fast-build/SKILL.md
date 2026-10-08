---
name: lean-fast-build
description: Ship a working, maintainable software vertical slice quickly with minimal turns. Use for fast-build requests, usage-limit pressure, or requests to build a website, app, API, agent, theme, or script quickly.
---

# Lean Fast-Build

Speed comes from sequencing and avoiding rework—not from skipping quality.

## Protocol
1. **Intake once.** If the request is buildable, do not ask questions. If one missing detail is critical, ask one question with a default.
2. **Plan briefly.** State the stack, file tree, core user path, and acceptance check in ≤8 lines.
3. **Vertical slice first.** Make the smallest end-to-end path runnable before expanding scope.
4. **Batch work.** Group independent edits. Avoid repeated rewrites of the same file.
5. **Quality floor.** Validate inputs, handle expected failures, keep secrets in environment variables, use clear names, and avoid speculative abstractions.
6. **UI floor.** If applicable: semantic HTML, keyboard access, responsive layout, readable contrast, loading/error/empty states.
7. **Verification.** Run the strongest available smoke test, build, typecheck, lint, or unit test. Report the actual result.
8. **Checkpoint.** Maintain `HANDOFF.md` when the work may span turns or the user asks for resumability.

## If time/usage is constrained
Finish the current vertical slice. Stop adding scope. Update `HANDOFF.md` and give the exact resume instruction: `Read HANDOFF.md and continue from Next.`

## Never skip
Correctness, security, destructive-action confirmation, validation, and the runnable check.
