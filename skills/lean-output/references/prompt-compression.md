# Prompt compression rules

1. Remove greetings, throat-clearing, repeated conclusions, and decorative prose.
2. Merge duplicate rules; keep the strongest precise version.
3. Replace repeated wording with a defined term or compact table.
4. Preserve every requirement, prohibition, exception, edge case, and output constraint.
5. Keep examples only when they disambiguate behavior; otherwise remove or consolidate them.
6. Move rarely needed background into an on-demand reference instead of deleting it.
7. Prefer imperative, testable language: `Do X`, `Never Y`, `If Z, then W`.
8. Avoid vague optimization claims such as "save as many tokens as possible" without a measurable criterion.
9. After compression, compare headings/rules and re-run the token audit.
