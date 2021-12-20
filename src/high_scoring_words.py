from collections import Counter
from dataclasses import dataclass
import src.constants as c
import src.utils as utils


@dataclass
class ScrabbleWord:
    """
    A data holder for scrabble words
    :param word: the word string
    :param scrabble_value: the game value of the word based on its characters
    :param character_counts: a Counter object for the characters in the word
    """
    word: str
    scrabble_value: int
    character_counts: Counter
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.word == other.word
    
    def __hash__(self):
        # Required for hashable test assertions
        return hash(self.word)

    def __lt__(self, other):
        if self.scrabble_value == other.scrabble_value:
            return self.word > other.word
        return self.scrabble_value < other.scrabble_value


class HighScoringWords:
    """
    A class used to represent high scoring Scrabble leaderboards from word lists and provided tiles
    """
    MAX_LEADERBOARD_LENGTH = 100  # The maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # Words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, valid_words_path: str = c.VALID_WORDS_PATH, letter_values_path: str = c.LETTER_VALUES_PATH):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param valid_words_path: a path to the text file containing the complete set of valid words, one word per line
        :param letter_values_path: a text file containing the score for each letter in the format letter:score one per line
        """
        self.valid_words = utils.read_valid_words(valid_words_path)
        self.letter_values = utils.read_letter_values(letter_values_path)
        self.sorted_scrabble_words = sorted(self.create_scrabble_word_objects(), reverse=True)
        
    def create_scrabble_word_objects(self) -> list[ScrabbleWord]:
        """
        Build a list of ScrabbleWord objects for each word in the complete set of valid words
        :return: the list of ScrabbleWord objects for each word.
        """
        scrabble_words = []
        for word in self.valid_words:
            if len(word) >= self.MIN_WORD_LENGTH:
                scrabble_value = sum([self.letter_values[letter] for letter in word])
                character_counts = Counter(word)
                scrabble_words.append(
                    ScrabbleWord(word, scrabble_value, character_counts)
                )
        return scrabble_words

    def build_leaderboard_for_word_list(self) -> list[str]:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words from the complete set of valid words
        :return: the list of top words by scrabble value
        """
        leaderboard_words = [scrabble_word.word for scrabble_word in self.sorted_scrabble_words]
        return leaderboard_words[:self.MAX_LEADERBOARD_LENGTH]

    def build_leaderboard_for_letters(self, starting_letters: str) -> list[str]:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters
        contained in the starting_letters String. The number of occurrences of a letter in the startingLetters String
        IS significant. If the starting letters are bulx, the word "bull" is NOT valid. There is only one l in the
        starting string but bull contains two l characters. Words are ordered in the leaderboard by their score
        (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the test_word_list.txt file
        :return: the list of top matching scrabble words
        """
        matching_words = []
        starting_letter_counts = Counter(starting_letters)
        
        for scrabble_word in self.sorted_scrabble_words:
            # Counters can be subtracted and are "falsy" when empty
            if not (scrabble_word.character_counts - starting_letter_counts):
                matching_words.append(scrabble_word.word)
            if len(matching_words) == self.MAX_LEADERBOARD_LENGTH:
                break
            
        return matching_words
