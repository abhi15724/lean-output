# Benchmark method

No results are published here because none have been measured yet. Measure your own.

## A/B
1. Pick 10 real tasks you actually do (explain, debug, write, refactor, research).
2. Run each in a fresh session twice: `/lean off`, then `/lean standard`.
3. `/lean-gain --last 20` gives output tokens and out/msg per session.

## Quality gate (do not skip)
Score each pair blind, 1-5, on: correct, complete, actionable, safe. A token win with a quality loss is a failure.
Report both: tokens saved, and quality delta.

## Expected shape
Largest savings where the baseline pads (chatty explanations, file echoes). Near zero where answers are already minimal.
