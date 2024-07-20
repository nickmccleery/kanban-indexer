import unittest

from kanban_indexer.alphabet_indexer import AlphabetIndexer


class TestAlphabetIndexer(unittest.TestCase):
    def test_full_range_midpoint(self):
        indexer = AlphabetIndexer("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(indexer.midpoint, "M")

    def test_adjacent_characters_midpoint(self):
        indexer = AlphabetIndexer("AB")
        self.assertEqual(indexer.midpoint, "A")

    def test_non_adjacent_characters_midpoint(self):
        indexer = AlphabetIndexer("ACEGIKMOQSUWY")
        self.assertEqual(indexer.midpoint, "M")

    def test_odd_length_alphabet_midpoint(self):
        indexer = AlphabetIndexer("ABCDEFG")
        self.assertEqual(indexer.midpoint, "D")

    def test_even_length_alphabet_midpoint(self):
        indexer = AlphabetIndexer("ABCDEF")
        self.assertEqual(indexer.midpoint, "C")

    def test_single_character_alphabet_midpoint(self):
        indexer = AlphabetIndexer("A")
        self.assertEqual(indexer.midpoint, "A")

    def test_start_property(self):
        indexer = AlphabetIndexer("ABCDEFG")
        self.assertEqual(indexer.start, "A")

    def test_end_property(self):
        indexer = AlphabetIndexer("ABCDEFG")
        self.assertEqual(indexer.end, "G")

    def test_to_int_method(self):
        indexer = AlphabetIndexer("ABCDEFG")
        self.assertEqual(indexer.to_int("C"), 2)

    def test_to_char_method(self):
        indexer = AlphabetIndexer("ABCDEFG")
        self.assertEqual(indexer.to_char(2), "C")

    def test_invalid_alphabet_construction(self):
        with self.assertRaises(ValueError):
            AlphabetIndexer("ZYXWVUTSRQPONMLKJIHGFEDCBA")  # Not sorted
        with self.assertRaises(ValueError):
            AlphabetIndexer("ABCDEFFGHIJKLMNOPQRSTUVWXYZ")  # Duplicate 'F'


if __name__ == "__main__":
    unittest.main()
