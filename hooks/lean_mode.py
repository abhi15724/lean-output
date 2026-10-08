#!/usr/bin/env python3
"""Persist lean-output mode and inject only the context needed for the active mode."""
import json
import os
import re
from pathlib import Path

MODES = {"lite", "standard", "ultra", "fast-build", "off"}
CONFIG_DIR = Path(os.path.expanduser(os.getenv("LEAN_CONFIG_DIR", "~/.config/lean-output")))
CONFIG_FILE = CONFIG_DIR / "config.json"
MODE_FILE = CONFIG_DIR / "mode"


def load_config():
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def default_mode():
    env = os.getenv("LEAN_DEFAULT_MODE", "").strip().lower()
    if env in MODES:
        return env
    configured = str(load_config().get("defaultMode", "standard")).lower()
    return configured if configured in MODES else "standard"


def save_mode(mode):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    MODE_FILE.write_text(mode + "\n", encoding="utf-8")


def read_mode():
    try:
        mode = MODE_FILE.read_text(encoding="utf-8").strip().lower()
        return mode if mode in MODES else default_mode()
    except OSError:
        return default_mode()


def main():
    try:
        payload = json.load(__import__("sys").stdin)
    except (ValueError, OSError):
        payload = {}

    prompt = str(payload.get("prompt") or "").strip()
    lean_match = re.fullmatch(r"/(?:lean-output:)?lean(?:\s+(\S+))?", prompt, re.IGNORECASE)
    fast_match = re.match(r"/(?:lean-output:)?lean-fast-build\b", prompt, re.IGNORECASE)

    if lean_match:
        requested = (lean_match.group(1) or default_mode()).lower()
        save_mode(requested if requested in MODES else default_mode())
    elif fast_match:
        save_mode("fast-build")

    mode = read_mode()
    context = {
        "lite": "Be concise: remove filler and repetition while keeping complete answers.",
        "standard": "Use lean-output standard mode: answer first, keep structure tight, avoid unnecessary recap and narration.",
        "ultra": "Use lean-output ultra mode: terse, result-first, fragments allowed; preserve correctness and required warnings.",
        "fast-build": "Use lean-output standard mode plus the lean-fast-build protocol for software-building requests.",
        "off": "lean-output is disabled for this turn unless the user explicitly requests concise output."
    }[mode]

    if mode != "off" or fast_match:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": f"lean-output active mode: {mode}. {context}"
        }}))


if __name__ == "__main__":
    main()
