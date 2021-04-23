import pytest

import Lab20 as Lab20


def test_loop_word_check():
    words = ["sad", "flag", "nerd", "flask", "rope"]
    sols = [True, True, False, True, False]
    for word, sol in zip(words, sols):
        student = Lab20.loop_word_check(word, Lab20.QWERTY_HOME)
        assert student == sol


def test_set_word_check():
    words = ["sad", "flag", "nerd", "flask", "rope"]
    sols = [True, True, False, True, False]
    for word, sol in zip(words, sols):
        student = Lab20.set_word_check(word, Lab20.QWERTY_HOME)
        assert student == sol


def test_calc_percentage():
    subsets = [
        Lab20.QWERTY_HOME,
        Lab20.DVORAK_HOME,
        Lab20.QWERTY_TOP,
        Lab20.DVORAK_TOP,
        Lab20.QWERTY_HOME + Lab20.QWERTY_TOP,
    ]
    sols = [0.14, 2.18, 0.43, 0.01, 20.67]
    for ss, sol in zip(subsets, sols):
        student = Lab20.calc_percentage(ss, Lab20.loop_word_check)
        assert round(student, 2) == sol
        student = Lab20.calc_percentage(ss, Lab20.set_word_check)
        assert round(student, 2) == sol


def test_predicted_percentage():
    assert (
        Lab20.PREDICTED_PERCENTAGE != 0
    ), "Did you forget to fill in your predicted percentage?"


def test_predicted_speed_winner():
    assert (
        Lab20.PREDICTED_SPEED_WINNER != ""
    ), "Did you forget to fill in your predicted speed winner?"
