from collections import Counter
import unittest
from src.high_scoring_words import HighScoringWords, ScrabbleWord


class TestHighScoringWords(unittest.TestCase):
    def setUp(self):
        self.hsw = HighScoringWords(
            valid_words_path="resources/test_word_list.txt",
            letter_values_path="resources/test_letter_values.txt"
        )

    def test_min_word_length(self):
        words = [scrabble_word.word for scrabble_word in self.hsw.sorted_scrabble_words]
        shortest_word = min(words, key=len)
        self.assertGreaterEqual(
            len(shortest_word),
            self.hsw.MIN_WORD_LENGTH,
            f"Minimum word length should be {self.hsw.MIN_WORD_LENGTH}"
        )

    def test_max_leaderboard_length(self):
        self.hsw_large = HighScoringWords(
            valid_words_path="resources/test_word_list_large.txt",
            letter_values_path="resources/test_letter_values.txt"
        )
        self.assertLessEqual(
            len(self.hsw_large.build_leaderboard_for_word_list()),
            self.hsw.MAX_LEADERBOARD_LENGTH,
            f"Maximum leaderboard length should be {self.hsw.MAX_LEADERBOARD_LENGTH}"
        )
        
    def test_leaderboard_for_word_list(self):
        expected_leaderboard = ["strawberry", "cherry", "apple", "banana", "pear"]
        self.assertListEqual(
            self.hsw.build_leaderboard_for_word_list(),
            expected_leaderboard,
            "Word leaderboards should be correctly created"
        )
    
    def test_leaderboard_for_letters(self):
        letters = "cheyppalerr"
        expected_leaderboard = ["cherry", "apple", "pear"]
        self.assertListEqual(
            self.hsw.build_leaderboard_for_letters(letters),
            expected_leaderboard,
            "Leaderboard should be correctly created for provided letters"
        )
        
    def test_create_scrabble_word(self):
        # Hashes based on word only so other parameters are redundant here
        expected_scrabble_word = ScrabbleWord("pear", 6, Counter({"a": 1, "e": 1, "p": 1, "r": 1}))
        self.assertEqual(
            self.hsw.sorted_scrabble_words[-1].word,
            expected_scrabble_word,
            "Scrabble word object's word attribute should be correctly created"
        )

    def test_created_scrabble_character_counts(self):
        self.assertEqual(
            self.hsw.sorted_scrabble_words[-1].character_counts,
            Counter({"a": 1, "e": 1, "p": 1, "r": 1}),
            "Scrabble word object's character count should be correctly created"
        )
        
    def test_leaderboard_for_empty_input_letters(self):
        letters = ""
        self.assertListEqual(
            self.hsw.build_leaderboard_for_letters(letters),
            [],
            "Leaderboard should be empty for empty input letters"
        )
