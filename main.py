"""Trust Falls, No One Left to Catch Us: one-line office joke.

The entry is a single sentence about office life. The setup is a team
building exercise, trust falls, and the punchline is that the company
just laid off the very people who would have caught you. The program
writes exactly that one line, and nothing else, to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "Our team building exercise was trust falls, which is bold for a "
    "company that just laid off the people who would have caught us."
)


def main():
    if JOKE.strip() != JOKE:
        raise ValueError("joke has stray leading or trailing whitespace")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1 to 200 characters, got %d" % len(JOKE))
    if "  " in JOKE:
        raise ValueError("joke has a double space")
    if not JOKE.endswith(".") or JOKE.count(".") != 1:
        raise ValueError("joke must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("entry.txt mismatch, got %r" % written)


if __name__ == "__main__":
    main()
