"""Count words, characters, sentences, and non-empty paragraphs."""

import argparse
from pathlib import Path
import re
import sys


WORD_PATTERN = re.compile(r"\b[^\W_]+(?:['’\-][^\W_]+)*\b", re.UNICODE)
SENTENCE_PATTERN = re.compile(r"[.!?]+(?:[\"'”’)\]]*)?(?=\s|$)")


def count_text(text):
    """Return text metrics. Characters include spaces and line breaks."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    paragraphs = [part for part in re.split(r"(?:\r?\n)[ \t]*(?:\r?\n)+", text) if part.strip()]
    return {
        "words": len(WORD_PATTERN.findall(text)),
        "characters": len(text),
        "characters_without_whitespace": sum(not char.isspace() for char in text),
        "sentences": len(SENTENCE_PATTERN.findall(text)),
        "paragraphs": len(paragraphs),
    }


def read_input(path=None, text=None):
    """Read explicit text, a UTF-8 file, or standard input."""
    if text is not None:
        return text
    if path is not None:
        source = Path(path)
        if not source.is_file():
            raise ValueError(f"Not a regular file: {source}")
        try:
            return source.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise ValueError(f"Could not read UTF-8 text file: {exc}") from exc
    if sys.stdin.isatty():
        print("Type or paste text, then finish with Ctrl+Z and Enter (Windows).", file=sys.stderr)
    return sys.stdin.read()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--file", help="read a UTF-8 text file")
    source.add_argument("--text", help="analyze this text directly")
    args = parser.parse_args()
    try:
        text = read_input(path=args.file, text=args.text)
    except ValueError as exc:
        parser.error(str(exc))
    for label, value in count_text(text).items():
        print(f"{label.replace('_', ' ').capitalize()}: {value}")


if __name__ == "__main__":
    main()
