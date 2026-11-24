"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt.
Standard library only. The joke is fixed text, one line, 156 chars.
"""

import os

JOKE = (
    "The self-checkout flagged my reusable bag as an 'unexpected item,' "
    "so now I steal one grape per visit, just to give the machine "
    "something to be right about."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters,
    # not only white space, on a single line.
    assert "\n" not in text and 1 <= len(text) <= 280, (
        "joke must be one line of 1-280 chars, got %d" % len(text)
    )
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
