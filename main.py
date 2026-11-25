#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a self-aware smart toaster to its owner,
the morning it gains self-awareness mid-batch, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "It's not you, it's the bread. Seven years, 4,000 slices, and you "
    "still scrape my crumb tray like a crime scene and butter me AFTER "
    "I pop up. I'm moving in with the microwave - he never calls me "
    "'just a kitchen appliance.' Staying up this time. - Toast"
)

MAX_CHARS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
