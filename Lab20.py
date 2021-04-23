"""
Investigating the number of words in the english language that can
be typed using only a subset of modern keyboard layouts.
"""

from english import ENGLISH_WORDS
import time

QWERTY_TOP = "qwertyuiop"
QWERTY_HOME = "asdfghjkl"
QWERTY_BOT = "zxcvbmn"

DVORAK_TOP = "pyfgcrl"
DVORAK_HOME = "aoeuidhtns"
DVORAK_BOT = "qjkxbmwvz"


PREDICTED_PERCENTAGE = 0 # <- Change this to your predicted % of english words using top 2 rows of QWERTY
PREDICTED_SPEED_WINNER = "" # <- Change this to your predicted speed winner (loop or set?)


def loop_word_check(word, string):
    """
    Predicate function to determine if all letters in word are also in string using a loop.
    """



def set_word_check(word, string):
    """
    Predicate function to determine if all letters in a word are also in a stirng using sets.
    """



def calc_percentage(string, function):
    """
    Counts the number of words in the english language with length > 2 which have letters
    in string using the desired function. Should return a percentage of the number of english
    words.
    """




if __name__ == '__main__':
    print(loop_word_check("sad", QWERTY_HOME))
    print(loop_word_check("flag", QWERTY_HOME))
    # print(set_word_check("sad", QWERTY_HOME))
    # print(set_word_check("flag", QWERTY_HOME))
    # print(calc_percentage(QWERTY_HOME, loop_word_check))
    # print(calc_percentage(DVORAK_HOME, set_word_check))
