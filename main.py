#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun bounty entry.

Writes exactly one emoji to the entry file. Stdlib only, deterministic,
no network, no clock, no randomness.
"""

import os
import unicodedata

EMOJI = "\U0001faf6"  # HEART HANDS


def validate_single_emoji(text: str) -> None:
    """Require the entry text to be exactly one emoji and nothing else.

    One grapheme cluster, no words, no whitespace, no extra characters.
    Heart Hands is a single code point, so a one-character check plus a
    symbol-category check pins it down exactly.
    """
    if len(text) != 1:
        raise ValueError(f"entry must be exactly one emoji, got {len(text)} characters")
    if text != text.strip() or text.isspace():
        raise ValueError("entry must not contain whitespace")
    if unicodedata.category(text) not in ("So", "Sk"):
        raise ValueError(f"entry is not an emoji/symbol: U+{ord(text):04X}")


def resolve_output_path() -> str:
    """Pick the output path, falling back if /output is not writable."""
    override = os.environ.get("MAKEFUN_OUTPUT")
    if override:
        return override
    try:
        os.makedirs("/output", exist_ok=True)
        probe = os.path.join("/output", ".write-test")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("")
        os.remove(probe)
        return "/output/entry.txt"
    except OSError:
        return os.path.join(os.getcwd(), "output", "entry.txt")


def main() -> int:
    validate_single_emoji(EMOJI)
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Verify the written file by reading it back.
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    validate_single_emoji(written)
    if written != EMOJI:
        raise ValueError("read-back mismatch: file content differs from entry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
