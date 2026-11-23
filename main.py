#!/usr/bin/env python3
"""One Letter for Your Day — entry writer.

Writes the entry: a single letter, exactly one byte, no newline.
The letter is the whole entry — the gate demands precisely one
character (A-Z) in /output/entry.txt, so this program writes one
byte and then reads it back to prove the byte is exactly right.
"""

import os
import sys

LETTER = "K"  # K — knackered. The day, honestly reported.


def output_path() -> str:
    """Entry destination: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(path: str) -> None:
    """Write exactly one byte — the letter, no newline, nothing else."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(LETTER.encode("ascii"))


def verify_entry(path: str) -> None:
    """Read the file back and demand exactly one character, A-Z.

    A trailing newline would make the file 2 bytes and fail the
    gate, so the check is on the raw bytes, not the decoded text.
    """
    with open(path, "rb") as handle:
        raw = handle.read()
    if len(raw) != 1:
        raise SystemExit(f"entry must be exactly 1 byte, got {len(raw)}: {raw!r}")
    char = raw.decode("ascii")
    if not ("A" <= char <= "Z"):
        raise SystemExit(f"entry must be one letter A-Z, got {char!r}")


def main() -> int:
    path = output_path()
    write_entry(path)
    verify_entry(path)
    print(f"wrote {path}: {LETTER!r} (1 byte)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
