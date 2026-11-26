"""One Line to Your Younger Self — Akun 1 (@walta-exchange), make.fun.

Reviser rewrite (from scratch): writes one single line to entry.txt in
MAKEFUN_OUTPUT_DIR (or /output when unset). Pure Python standard library,
no dependencies, no network.

Reviser verdict on the builder line: it was good — the torn-shoes image
and the laugher-becomes-wife turn were real — but it had two genuine
weaknesses against the judge brief. First, a pronoun shift: it opens
"Kid" (you) then tells the story about "the boy" in the third person,
so its core clause talks about the younger self instead of to him.
Second, its tail, "stay kind", is a motto anyone could say, which
dilutes criterion 2 (only this older self could say it) and blunts
criterion 5 (honest enough to sting). The revised line fixes both:
direct "you" all the way through, the same turn kept, and the advice
tied to the image itself — "stop hiding them, and learn to fix them
yourself" — a concrete, slightly stinging, lived instruction instead
of generic kindness. One sentence, 111 characters, inside the
200-character gate.
"""

import os

ENTRY = (
    "Kid, the girl laughing at your torn shoes will marry you "
    "\u2014 so stop hiding them, and learn to fix them yourself."
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
