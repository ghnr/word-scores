from dataclasses import dataclass
from operator import attrgetter


@dataclass
class ScrabbleWord:
    word: str
    scrabble_value: int

    def __lt__(self, other):
        return (-self.scrabble_value, self.word) > (-other.scrabble_value, other.word)


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, valid_words='wordlist.txt', letter_values='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param valid_words: a text file containing the complete set of valid words, one word per line
        :param letter_values: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        with open(valid_words) as f:
            self.valid_words = f.read().splitlines()

        with open(letter_values) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self) -> list:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """
        scrabble_words = []
        for word in self.valid_words:
            scrabble_value = sum([self.letter_values[letter] for letter in word])
            scrabble_words.append(ScrabbleWord(word, scrabble_value))
        
        sorted_scrabbled_words = sorted(scrabble_words, reverse=True)
        return sorted_scrabbled_words[:self.MAX_LEADERBOARD_LENGTH]

    def build_leaderboard_for_letters(self, starting_letters: str) -> list:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters
        contained in the starting_letters String. The number of occurrences of a letter in the startingLetters String
        IS significant. If the starting letters are bulx, the word "bull" is NOT valid. There is only one l in the
        starting string but bull contains two l characters. Words are ordered in the leaderboard by their score
        (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """
        return []


if __name__ == '__main__':
    high_scoring_words = HighScoringWords()
    word_leaderboard = high_scoring_words.build_leaderboard_for_word_list()
    print(word_leaderboard)
