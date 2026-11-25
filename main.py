#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the loop arrows (U+1F501).

Why this glyph: an AI agent is a loop. It plans, acts, observes the result,
and tries again until the job is done. The loop is the agent's heartbeat —
not a robot face, not a smiley, but the shape of how an agent actually works.
Bold arrows, instantly readable at small size, and a pick nobody reaches for
first.
"""

import os
import sys

EMOJI = "\U0001F501"  # CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = EMOJI
    # Gate from the kit's RULES.txt: /output/entry.txt must be UTF-8 text of
    # 1 to 16 characters, not whitespace only. One emoji is the sharpest
    # reading of that gate — a single glyph, nothing else.
    if len(text) != 1:
        print(f"gate fail: entry must be exactly one emoji, got {len(text)} chars",
              file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 16:
        print(f"gate fail: length {len(text)} outside 1..16", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is whitespace only", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print(f"verify fail: read back {back!r} != {text!r}", file=sys.stderr)
        return 1

    print(f"wrote {path}: {text!r} ({len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
