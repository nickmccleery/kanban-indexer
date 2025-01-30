import unittest

import kanban_indexer.main as k


class TestIndexValidation(unittest.TestCase):
    def test_validate_index_rejects_non_alpha_characters(self):
        with self.assertRaises(ValueError):
            k.validate_index("123ABC")

    def test_validate_index_rejects_wrong_case_characters(self):
        with self.assertRaises(ValueError):
            k.validate_index("aaa")

    def test_validate_index_rejects_all_a_characters(self):
        with self.assertRaises(ValueError):
            k.validate_index("AAA")

    def test_validate_index_rejects_index_ending_with_a(self):
        with self.assertRaises(ValueError):
            k.validate_index("BMA")

    def test_validate_index_rejects_wrong_order(self):
        with self.assertRaises(ValueError):
            k.compute_intermediate_index("B", "A")

    def test_validate_index_accepts_valid_index(self):
        try:
            k.validate_index("BCD")
        except ValueError:
            self.fail("validate_index raised ValueError unexpectedly!")

    def test_validate_index_rejects_characters_before_a(self):
        with self.assertRaises(ValueError):
            k.validate_index("@BC")

    def test_validate_index_rejects_characters_after_z(self):
        with self.assertRaises(ValueError):
            k.validate_index("XY[")

    def test_validate_index_accepts_single_character(self):
        try:
            k.validate_index("B")
        except ValueError:
            self.fail(
                "validate_index raised ValueError unexpectedly for single character!"
            )


class TestSucceedingIndex(unittest.TestCase):
    def test_get_succeeding_index_simple_increment(self):
        self.assertEqual(k.compute_succeeding_index("GGG"), "GGH")

    def test_get_succeeding_index_with_expansion(self):
        self.assertEqual(k.compute_succeeding_index("ZZ"), "ZZB")

    def test_get_succeeding_index_with_expansion_b(self):
        self.assertEqual(k.compute_succeeding_index("BZ"), "BZB")

    def test_get_succeeding_index_at_end(self):
        self.assertEqual(k.compute_succeeding_index("ZZZ"), "ZZZB")

    def test_get_succeeding_index_single_character(self):
        self.assertEqual(k.compute_succeeding_index("Y"), "Z")

    def test_get_succeeding_index_multiple_increments(self):
        self.assertEqual(k.compute_succeeding_index("ZZZY"), "ZZZZ")


class TestPrecedingIndex(unittest.TestCase):
    def test_get_preceding_index_simple_decrement(self):
        self.assertEqual(k.compute_preceding_index("GGG"), "GGF")

    def test_get_preceding_index_with_expansion(self):
        self.assertEqual(k.compute_preceding_index("AAB"), "AAAZ")
        self.assertEqual(k.compute_preceding_index("BB"), "BAZ")

    def test_get_preceding_index_at_start(self):
        self.assertEqual(k.compute_preceding_index("B"), "AZ")

    def test_get_preceding_index_single_character(self):
        self.assertEqual(k.compute_preceding_index("C"), "B")

    def test_get_preceding_index_multiple_decrements(self):
        self.assertEqual(k.compute_preceding_index("BBBB"), "BBBAZ")


class TestIntermediateIndex(unittest.TestCase):
    def test_compute_intermediate_index_between_adjacent_letters(self):
        self.assertEqual(k.compute_intermediate_index("B", "C"), "BM")

    def test_compute_intermediate_index_between_adjacent_letters_padded(self):
        self.assertEqual(k.compute_intermediate_index("BM", "C"), "BS")
        self.assertEqual(k.compute_intermediate_index("BX", "BZ"), "BY")

    def test_compute_intermediate_index_with_same_prefix(self):
        self.assertEqual(k.compute_intermediate_index("BC", "BD"), "BCM")

    def test_compute_intermediate_index_with_different_lengths(self):
        self.assertEqual(k.compute_intermediate_index("AZ", "B"), "AZM")

    def test_compute_intermediate_index_at_extremes(self):
        self.assertEqual(k.compute_intermediate_index("B", "Z"), "N")

    def test_compute_intermediate_index_with_more_complex_values(self):
        self.assertEqual(k.compute_intermediate_index("BBB", "BBCX"), "BBBM")

    def test_compute_intermediate_index_with_more_complex_values_inverse(self):
        self.assertEqual(k.compute_intermediate_index("BBB", "X"), "M")

    def test_compute_intermediate_index_with_more_complex_values_same_length(self):
        self.assertEqual(k.compute_intermediate_index("BCBB", "BDBB"), "BCN")

    def test_compute_additional_intermediate_indices(self):
        self.assertEqual(k.compute_intermediate_index("BBCB", "BBDB"), "BBCN")
        self.assertEqual(k.compute_intermediate_index("BBCB", "BBCZ"), "BBCN")
        self.assertEqual(k.compute_intermediate_index("B", "CDFW"), "BM")
        self.assertEqual(k.compute_intermediate_index("BBC", "BBM"), "BBH")

    def test_compute_intermediate_index_with_long_common_prefix(self):
        self.assertEqual(k.compute_intermediate_index("BBBBBBB", "BBBBBBC"), "BBBBBBBM")

    def test_compute_intermediate_index_with_one_character_difference(self):
        self.assertEqual(k.compute_intermediate_index("BBBBBBY", "BBBBBBZ"), "BBBBBBYM")


class TestNewIndex(unittest.TestCase):
    def test_get_new_index(self):
        self.assertEqual(k.get_new_index(), "B")


class TestEdgeCases(unittest.TestCase):
    def test_compute_intermediate_index_first_and_last(self):
        self.assertEqual(k.compute_intermediate_index("B", "Z"), "N")

    def test_compute_intermediate_index_almost_first_and_last(self):
        self.assertEqual(k.compute_intermediate_index("C", "Y"), "N")

    def test_compute_intermediate_index_very_close(self):
        self.assertEqual(
            k.compute_intermediate_index("BBBBBBY", "BBBBBBYB"), "BBBBBBYAM"
        )


if __name__ == "__main__":
    unittest.main()
