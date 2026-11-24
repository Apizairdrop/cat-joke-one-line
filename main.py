"""The One-Line Cat Joke That Lands — make.fun entry.

Writes exactly one joke line (118 characters) to /output/entry.txt.
Nothing else is written to the entry file.
"""

import os

JOKE = "I told my cat he's adopted; he looked at me like he'd known all along and I was the last one in the house to find out."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, and a single line — nothing else in the entry.
assert JOKE == JOKE.strip(), "joke must have no leading/trailing whitespace"
assert "\n" not in JOKE, "joke must be a single line"
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
