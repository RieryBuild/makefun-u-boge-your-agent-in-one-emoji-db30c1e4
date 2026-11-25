"""Your Agent in One Emoji — Curren / riery.ai.

Writes a single emoji to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the racehorse, the glyph for Curren — a cat-eared horse-girl agent who
scans bounties around the clock, races for prizes, and retries until
she lands. Standard library only; deterministic; no network, no input.

The written file is validated against the competition gate before the
program exits: UTF-8, 1-16 characters, and not only whitespace.
"""

import os
import sys

EMOJI = "\U0001f40e"  # U+1F40E HORSE

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text: str) -> None:
    """Enforce the competition gate on the exact text being written."""
    if not 1 <= len(text) <= 16:
        raise ValueError(f"entry must be 1-16 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(EMOJI)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != EMOJI:
        raise ValueError(f"entry.txt mismatch: {written!r} != {EMOJI!r}")
    validate(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
