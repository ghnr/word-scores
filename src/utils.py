def read_valid_words(valid_words_path: str) -> list[str]:
    """
    :param valid_words_path: a path to the text file containing the complete set of valid words, one word per line
    :rtype: a list of valid words
    """
    with open(valid_words_path) as f:
        return f.read().splitlines()
    

def read_letter_values(letter_values_path: str) -> dict[str, int]:
    """
    :param letter_values_path: a text file containing the score for each letter in the format letter:score one per line
    :rtype: dictionary of lower-case letter (key) to scrabble value (value)
    """
    with open(letter_values_path) as f:
        letter_values = {}
        for line in f:
            (key, val) = line.split(':')
            letter_values[str(key).strip().lower()] = int(val)
        return letter_values
