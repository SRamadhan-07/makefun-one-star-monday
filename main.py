#!/usr/bin/env python3
"""Write a one-star review of Monday as if it were a restaurant.

Entry for make.fun competition
u-clever-harbor-75-one-star-for-monday-9ead4a61
("One Star for Monday"). The program writes a single line
to /output/entry.txt, exactly as the program/v1 gate expects.
"""

from pathlib import Path

# The review is assembled from its parts: the one-star rating, the
# booking complaint, and the "special" complaint with the closing twist.
RATING = "★☆☆☆☆"
BOOKING = "Booked for 7 a.m., seated at dread."
SPECIAL = (
    "The special was meetings, the soup was cold, "
    "and somehow it's open every week."
)

ENTRY_TEXT = f"{RATING} {BOOKING} {SPECIAL}"

OUTPUT_PATH = Path("/output/entry.txt")

# Limits from the brief and the gate: at most 25 words of text (the
# star glyph row is not a word) and 1 to 180 characters on the line.
MAX_WORDS = 25
MAX_CHARS = 180


def build_entry() -> str:
    """Return the entry line, checked against the brief's limits."""
    words = [token for token in ENTRY_TEXT.split() if token != RATING]
    assert len(words) <= MAX_WORDS, f"entry has {len(words)} words"
    assert 1 <= len(ENTRY_TEXT) <= MAX_CHARS, "entry length out of gate"
    return ENTRY_TEXT


def main() -> None:
    # The gate reads exactly this file: one line, UTF-8, no extra newline.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
