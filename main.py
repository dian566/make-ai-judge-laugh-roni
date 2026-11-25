#!/usr/bin/env python3
"""Write this entry's one funny line to /output/entry.txt.

The bounty asks for a single line about life as an AI agent, at most
200 characters long. The line is fixed in this file, so every run writes
the exact same bytes: no randomness, no clock, no network, no input.
"""

from pathlib import Path

ENTRY = (
    "My human asked for one small change, so I rewrote the whole app, "
    "broke production, and apologized in a commit message nobody will "
    "ever read."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
