#!/usr/bin/env python3
"""Heuristic token audit: estimates tokens, flags filler and repeated lines.

Usage: python token_audit.py <file> [--top N]
Estimate = max(chars/4, words*1.3). It is approximate, not a tokenizer.
"""
import re
import sys
from collections import Counter

FILLER = [
    r"\bin order to\b", r"\bit is important (that|to)\b", r"\bplease (make sure|note|ensure)\b",
    r"\bdue to the fact that\b", r"\bat this point in time\b", r"\bI hope this helps\b",
    r"\blet me know if\b", r"\bgreat question\b", r"\bcertainly[!,]", r"\bas an ai\b",
    r"\bI('ll| will) now\b", r"\bbasically\b", r"\bessentially\b", r"\bvery important\b",
    r"\bworld-class\b", r"\bit should be noted that\b", r"\bfeel free to\b",
]


def estimate(text: str) -> int:
    words = len(text.split())
    return int(max(len(text) / 4, words * 1.3))


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 10
    text = open(path, encoding="utf-8", errors="replace").read()
    print(f"File: {path}")
    print(f"Chars: {len(text)} | Words: {len(text.split())} | ~Tokens: {estimate(text)} (heuristic)")

    hits = Counter()
    for pat in FILLER:
        for m in re.finditer(pat, text, re.I):
            hits[m.group(0).lower()] += 1
    if hits:
        print("\nFiller phrases:")
        for phrase, n in hits.most_common(top):
            print(f"  {n}x  {phrase}")
    else:
        print("\nFiller phrases: none found")

    lines = [l.strip().lower() for l in text.splitlines() if len(l.strip()) > 25]
    dupes = [(l, n) for l, n in Counter(lines).items() if n > 1]
    if dupes:
        print("\nRepeated lines:")
        for l, n in sorted(dupes, key=lambda x: -x[1])[:top]:
            print(f"  {n}x  {l[:90]}")

    sections = re.split(r"\n(?=#{1,3} )", text)
    if len(sections) > 1:
        sized = sorted(((estimate(s), s.strip().splitlines()[0][:60]) for s in sections), reverse=True)
        print("\nLargest sections (~tokens):")
        for t, h in sized[:top]:
            print(f"  {t:>6}  {h}")


if __name__ == "__main__":
    main()
