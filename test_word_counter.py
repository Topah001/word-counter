import tempfile
import unittest
from pathlib import Path

from word_counter import count_text, read_input


class WordCounterTests(unittest.TestCase):
    def test_counts_prose_and_paragraphs(self):
        result = count_text("Hello, world! It's a test.\n\nSecond line?")
        self.assertEqual(result, {
            "words": 7, "characters": 40, "characters_without_whitespace": 33,
            "sentences": 3, "paragraphs": 2,
        })

    def test_empty_and_whitespace_input(self):
        self.assertEqual(count_text(" \n\n\t"), {
            "words": 0, "characters": 4, "characters_without_whitespace": 0,
            "sentences": 0, "paragraphs": 0,
        })

    def test_paragraphs_ignore_blank_lines_and_unicode_words(self):
        result = count_text("  Café—naïve!\n \n\nDon't stop.")
        self.assertEqual(result["words"], 4)
        self.assertEqual(result["paragraphs"], 2)
        self.assertEqual(result["sentences"], 2)

    def test_reads_explicit_text(self):
        self.assertEqual(read_input(text="ok"), "ok")

    def test_reads_utf8_file_and_rejects_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "story.txt"
            file.write_text("こんにちは.", encoding="utf-8")
            self.assertEqual(read_input(path=file), "こんにちは.")
            with self.assertRaises(ValueError):
                read_input(path=directory)

    def test_non_string_is_rejected(self):
        with self.assertRaises(TypeError):
            count_text(None)


if __name__ == "__main__":
    unittest.main()
