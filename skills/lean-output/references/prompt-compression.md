# Prompt / Document Compression

## High-yield cuts (in order)
1. **Duplicates**: same rule stated twice in different words. Keep the clearer one.
2. **Preamble and role fluff**: "You are a world-class expert...". Keep a one-line role only if it changes behavior.
3. **Hedging and filler**: "please make sure to", "it is important that", "in order to" -> "to".
4. **Explaining the obvious**: instructions a capable model already follows by default.
5. **Long examples**: keep one tight example per behavior; shorten the rest to pattern + one line.
6. **Verbose formatting**: heavy banners, repeated headers, decorative symbols.
7. **Negative piles**: replace five "don't" lines with one positive instruction describing the target.

## Rewrite patterns
| Before | After |
|---|---|
| In order to | To |
| It is important that you always | Always |
| Due to the fact that | Because |
| You should make sure to include | Include |
| At this point in time | Now |
| Provide a detailed explanation of | Explain |

## Structure wins
- Table instead of repeated "If X then Y" sentences.
- Reference files for rarely-needed detail (load on demand) instead of inlining everything.
- Keep always-loaded text (descriptions, system prompts) tiny; move detail into on-demand files.

## Don't compress
- Exact strings, schemas, field names, regexes, commands.
- Numbers, thresholds, constraints.
- The one example that defines a tricky format.

## Verify
After compressing, diff the rule lists: nothing lost, nothing changed in meaning. Test on 2-3 real prompts if possible.
