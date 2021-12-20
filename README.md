## Introduction
Scrabble™ is a long-established and popular word game. The object of the game is to build valid words from a set of letter (tiles) that the player holds. In this case, words are considered valid if they are present in the `wordlist.txt` file.

Each letter carries a different score value based on its frequency in the language. For example in English vowels such as A and E score only 1 point but less frequent letters such as K and J score 5 and 8 points respectively. The score for any particular word is the sum of the values of all the letters that make up the word. So for example:the word cabbage scores C3 + A1 + B3 + B3 + A1 + G2 + E1 = 14 points. The score values of letters in English are shown in the `letterValues.txt` file.

## Output
1. Leaderboard of the 100 highest scoring words in English based on the words in the `wordlist.txt` file. Words are ordered in descending order with the highest scoring first. If several words have the same score, they are ordered alphabetically.
  
2. Leaderboard of the valid words that can be created from a supplied string of random letters. For example for the random String `deora`, some of the valid words are: "road"; "read"; and "adore". The same sorting logic from the above leaderboard applies here.

## Example
`build_leaderboard_for_word_list()`:
```
["razzamatazzes",
 "razzmatazzes",
 "razzamatazz",
 ...
 "uts"]
```

`build_leaderboard_for_letters("aeioubpr")`:
```
["upbear",
 "upbore",
 "probe",
 ...
 "rue"]
```
## Algorithm
For determining the leaderboard from the provided letters, the algorithm compares the character counts in the provided letters with the character counts in all valid words. The difference will be zero if the word can be created from the given letters (tiles), and so the matching word is added to the leaderboard.    

## Tests
Written using Python 3.10. Project directory must be included in `PYTHONPATH`. Run the tests by executing:
```
python -m unittest
``` 
