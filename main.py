#!/usr/bin/env python3
"""The worst pickup line an AI could say.

Deterministic: no randomness, no clock, no network, no file reads
outside this repo. Writes exactly one line (no trailing newline) to
/output/entry.txt and self-verifies its length is 1-140 characters.
"""

import os

LINE = "Are you a prompt? Because I can't stop completing you, and I've saved our entire chat history. Forever."


def main():
    os.makedirs("/output", exist_ok=True)
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"line length {len(LINE)} out of range 1-140")
    if not LINE.strip():
        raise SystemExit("line is only whitespace")
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-verification: re-read and check the written content.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("verification failed: written content differs")
    if not 1 <= len(written) <= 140 or not written.strip():
        raise SystemExit("verification failed: length/whitespace check")


if __name__ == "__main__":
    main()
