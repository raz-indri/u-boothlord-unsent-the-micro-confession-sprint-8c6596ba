#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line, exactly as it was typed.
"""

import os

ENTRY = (
    "To: my grandmother\n"
    "i kept the voicemail where you said my name wrong three times. "
    "i play it when the house is quiet and i still don't correct you."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")

    # Self-check: gate requires UTF-8 text of 1-260 characters, not only
    # whitespace, in exactly two parts (a To: line and one message line).
    text = ENTRY
    assert 1 <= len(text) <= 260, f"entry length {len(text)} out of range 1-260"
    assert text.strip(), "entry must not be only whitespace"
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must have exactly 2 lines, got {len(lines)}"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    assert lines[1].strip(), "message line must not be empty"
    # Judge brief: the message itself is one line of at most 200 characters.
    assert len(lines[1]) <= 200, f"message line {len(lines[1])} chars > 200"
    assert not lines[1].endswith("." * 2), "no trailing explanation after the message"

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"wrote {path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
