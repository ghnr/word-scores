import unittest
import src.utils


class TestReadUtils(unittest.TestCase):
    def test_read_word_list(self):
        expected_word_list = ["apple", "banana", "cherry", "pear", "strawberry"]
        self.assertListEqual(
            src.utils.read_valid_words("resources/test_word_list.txt"),
            expected_word_list,
            "Should correctly read word list"
        )
        
    def test_read_letter_values(self):
        expected_letter_value_z = 10
        self.assertEqual(
            src.utils.read_letter_values("resources/test_letter_values.txt").get("z"),
            expected_letter_value_z,
            "Should correctly read letter values"
        )

    def test_letter_values_is_exhaustive(self):
        import string
        letters = list(src.utils.read_letter_values("resources/test_letter_values.txt").keys())
        self.assertCountEqual(
            letters,
            list(string.ascii_lowercase),
            "Letter values should have a value for each lower-case character in the English alphabet"
        )
