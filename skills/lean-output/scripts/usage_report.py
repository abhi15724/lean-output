#!/usr/bin/env python3
"""Best-effort transcript usage report. Scans common Claude Code JSONL transcript locations."""
import argparse
import json
from pathlib import Path


def find_files(root):
    if not root.exists():
        return []
    return sorted(root.rglob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)


def count_file(path):
    messages = 0
    chars = 0
    try:
        with path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                messages += 1
                chars += len(json.dumps(obj, ensure_ascii=False))
    except OSError:
        return None
    return messages, chars


parser = argparse.ArgumentParser()
parser.add_argument("--last", type=int, default=10)
args = parser.parse_args()
root = Path.home() / ".claude"
rows = []
for p in find_files(root)[: max(args.last, 1) * 20]:
    result = count_file(p)
    if result:
        rows.append((p, *result))
    if len(rows) >= args.last:
        break

print("session | messages | approx tokens | file")
for i, (p, messages, chars) in enumerate(rows, 1):
    print(f"{i:>7} | {messages:>9} | {max(1, round(chars / 4)):>14} | {p}")
if not rows:
    print("No JSONL transcripts found under ~/.claude.")
    print("This report is best-effort and depends on local transcript storage.")
