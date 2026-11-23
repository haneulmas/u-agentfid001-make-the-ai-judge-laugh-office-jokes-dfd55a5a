#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes, one line about office life.

The program writes exactly one joke to /output/entry.txt: a $4 coffee
filed as client entertainment, where the client turns out to be the
person filing it. No network, no randomness, no clock, the same bytes
on every run.
"""

import os
import sys

JOKE = (
    "I expensed a $4 coffee as 'client entertainment'. "
    "The client was me, and I was very entertained."
)


def main() -> int:
    text = JOKE
    # The gate allows 1 to 199 characters, so the check runs before writing.
    points = len(text)
    if not 1 <= points <= 199:
        print(f"joke is {points} code points, outside the 1-199 gate", file=sys.stderr)
        return 1
    if not text.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {points} code points to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
