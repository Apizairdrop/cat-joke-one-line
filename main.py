"""The One-Line Cat Joke That Lands — make.fun entry.

Writes exactly one joke line (118 characters) to /output/entry.txt.
Nothing else is written to the entry file.
"""

import os

JOKE = "I told my cat he's adopted; he looked at me like he'd known all along and I was the last one in the house to find out."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
