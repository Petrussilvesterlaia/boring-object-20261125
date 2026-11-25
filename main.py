#!/usr/bin/env python3
"""One-line review of the most boring everyday object.

Writes a single funny, true review line to /output/entry.txt for
make.fun's "The Most Boring Object, Reviewed in One Line" bounty.
The gate requires UTF-8 text of 1 to 200 characters, a single line,
not only white space.
"""

import sys

ENTRY = "The dustpan's only job is catching what the broom misses, yet it always leaves one thin line of dirt behind \u2014 a receipt for the job it never finished."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def validate_entry(text):
    """Check the entry against the competition gate. Returns a list of problems."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if len(text) > MAX_LENGTH:
        problems.append("entry is %d characters, over the %d limit" % (len(text), MAX_LENGTH))
    if not text.strip():
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry spans more than one line")
    for ch in text:
        if ord(ch) < 32 and ch not in ("\t",):
            problems.append("entry contains a control character U+%04X" % ord(ch))
    return problems


def validate_line_shape(text):
    """Check the line has no double spaces and no trailing space."""
    problems = []
    if "  " in text:
        problems.append("entry contains consecutive spaces")
    if text.endswith(" "):
        problems.append("entry ends with a space")
    if text.startswith(" "):
        problems.append("entry starts with a space")
    return problems


def main():
    problems = validate_entry(ENTRY) + validate_line_shape(ENTRY)
    if problems:
        for problem in problems:
            print("INVALID: %s" % problem, file=sys.stderr)
        return 1

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        read_back = f.read()

    if read_back != ENTRY:
        print("INVALID: read-back differs from the entry", file=sys.stderr)
        return 1

    print("OK: wrote %d characters to %s (gate + line-shape checks passed)"
          % (len(ENTRY), OUTPUT_PATH))
    print("Entry: %s" % ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
