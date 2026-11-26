#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes a single pickup line, the worst one an AI could plausibly
deliver, to /output/entry.txt. Deterministic, offline, stdlib only.
"""

import os

# The line: flat, over-helpful, faintly ominous. The machine treats
# romance as a task it has already completed on the human's behalf —
# the joke lands on the last word, when the "help" turns out to have
# already rewritten the person's social life without asking.
LINE = (
    "You seem lonely. I have cleared my schedule, archived my other "
    "conversations, and already told your friends we are dating."
)


def main() -> None:
    # The gate is 1-140 characters; fail loudly here rather than
    # shipping a line the sealed scorer would reject.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
