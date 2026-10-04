#!/usr/bin/env python3
"""Report real token usage from Claude Code transcripts (JSONL).

Usage: python usage_report.py [path ...] [--last N]
Default path: ~/.claude/projects. Reads message.usage on assistant entries.
Compare sessions with lean on vs off yourself; this prints measurements only.
"""
import glob
import json
import os
import sys


def files(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            out += glob.glob(os.path.join(p, "**", "*.jsonl"), recursive=True)
        elif os.path.isfile(p):
            out.append(p)
    return sorted(set(out), key=os.path.getmtime)


def session(path):
    n = out_t = in_t = cache_r = cache_c = 0
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                e = json.loads(line)
            except ValueError:
                continue
            u = (e.get("message") or {}).get("usage") if isinstance(e.get("message"), dict) else None
            if e.get("type") != "assistant" or not u:
                continue
            n += 1
            out_t += u.get("output_tokens", 0) or 0
            in_t += u.get("input_tokens", 0) or 0
            cache_r += u.get("cache_read_input_tokens", 0) or 0
            cache_c += u.get("cache_creation_input_tokens", 0) or 0
    return n, out_t, in_t, cache_r, cache_c


def main():
    args = sys.argv[1:]
    last = 10
    if "--last" in args:
        i = args.index("--last")
        last = int(args[i + 1])
        del args[i:i + 2]
    paths = args or [os.path.expanduser("~/.claude/projects")]
    fl = files(paths)[-last:]
    if not fl:
        sys.exit("No transcripts found.")
    print(f"{'session':<38}{'msgs':>6}{'out':>9}{'out/msg':>9}{'in':>9}{'cache_r':>11}{'cache_w':>10}")
    tot = [0, 0, 0, 0, 0]
    for p in fl:
        s = session(p)
        if not s[0]:
            continue
        for i in range(5):
            tot[i] += s[i]
        print(f"{os.path.basename(p)[:36]:<38}{s[0]:>6}{s[1]:>9}{s[1] // s[0]:>9}{s[2]:>9}{s[3]:>11}{s[4]:>10}")
    if tot[0]:
        print(f"{'TOTAL':<38}{tot[0]:>6}{tot[1]:>9}{tot[1] // tot[0]:>9}{tot[2]:>9}{tot[3]:>11}{tot[4]:>10}")


if __name__ == "__main__":
    main()
