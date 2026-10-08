#!/usr/bin/env python3
"""Heuristic token/byte audit for text files. Not an exact tokenizer."""
import re
import sys
from pathlib import Path


def audit(path):
    p = Path(path)
    text = p.read_text(encoding="utf-8", errors="replace")
    words = re.findall(r"\S+", text)
    chars = len(text)
    lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
    approx_tokens = max(1, round(chars / 4)) if text else 0
    print(f"file: {p}")
    print(f"bytes: {p.stat().st_size}")
    print(f"lines: {lines}")
    print(f"words: {len(words)}")
    print(f"approx_tokens: {approx_tokens}")
    print("note: heuristic estimate; tokenizer-specific counts may differ.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: token_audit.py <file>")
    audit(sys.argv[1])
