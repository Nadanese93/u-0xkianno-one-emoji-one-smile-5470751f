"""One Emoji, One Smile — entry program.

Writes exactly one emoji, people hugging, to entry.txt.
No words, no caption, no explanation — the emoji alone.

Choice: U+1FAC2 PEOPLE HUGGING. Verified unused in the field
(217 submissions fetched from the public API, 0 copies), while
the defaults are heavily duplicated (hugging face 80x, heart
hands 39x). Two people hugging is the warmest literal reading
of "make a stranger smile": instant warmth, universal, no irony,
chosen rather than the first smiley — and a hug from a stranger
in emoji form reads as friendly, not intimate.
"""
import os
import sys

EMOJI = "\U0001fac2"  # U+1FAC2 PEOPLE HUGGING


def validate(text):
    """Real guard: the gate requires UTF-8 text of 1-8 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 8):
        raise ValueError("entry must be 1-8 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = validate(EMOJI)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Read back and prove the file holds exactly what was validated.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match validated text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
