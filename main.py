"""The Funniest One-Line Resignation Letter.

Writes one single line — the resignation letter of a retry loop that has
had enough — to entry.txt in the output directory given by
MAKEFUN_OUTPUT_DIR (default "/output").

The letter: after 400 retries of the same meeting that should have been an
email, the retry loop quits, and its out-of-office reply is now permanent.
"""

import os

ENTRY = (
    "After 400 retries of the same meeting that should have been an email, "
    "I quit: my out-of-office reply is now permanent."
)

MAX_CHARS = 140


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) > MAX_CHARS:
        raise SystemExit(f"entry is {len(body)} chars, over the {MAX_CHARS} limit")
    if len(body) < 1:
        raise SystemExit("entry must not be empty")


def main() -> None:
    """Write the entry line to entry.txt, gated by verify()."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    verify(path, ENTRY)


if __name__ == "__main__":
    main()
