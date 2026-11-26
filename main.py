"""One Line to Your Younger Self — Akun 1 (@walta-exchange), make.fun.

Writes one single line to entry.txt in MAKEFUN_OUTPUT_DIR (or /output
when unset). Pure Python standard library, no dependencies, no network.

The line is spoken straight to the writer's younger self ("Kid, ... stay
kind, and keep the shoes"): one concrete lived moment — torn shoes laughed
at, fixed by the same boy — with a turn the reader does not see coming
(the girl who laughs marries the boy who fixed them). It stings a little,
lands in one breath, and explains nothing about itself. One sentence,
110 characters, inside the 200-character gate.
"""

import os

ENTRY = (
    "Kid, the girl who laughs at your torn shoes will marry the boy "
    "who fixed them \u2014 stay kind, and keep the shoes."
)

MAX_CHARS = 200


def build_entry():
    """Return the entry text exactly as it must be written."""
    return ENTRY


def validate_entry(text):
    """Raise ValueError unless the text passes the bounty gate."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-empty text")
    if text != text.strip():
        raise ValueError("entry must have no leading or trailing whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")


def write_entry(text, out_dir):
    """Validate, then write the entry directly to entry.txt (no temp file)."""
    validate_entry(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(build_entry(), out_dir)


if __name__ == "__main__":
    main()
