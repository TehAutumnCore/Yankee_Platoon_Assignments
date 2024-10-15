import pytest
from guessing_game import GuessingGame

def test_guess_high():
    game = GuessingGame(10)
    result = game.guess(15)
    assert result == 'high'

def test_guess_low():
    game = GuessingGame(10)
    result = game.guess(5)
    assert result == 'low'

def test_guess_correct():
    game = GuessingGame(10)
    result = game.guess(10)
    assert result == 'correct'

def test_solved_false():
    game = GuessingGame(10)
    assert game.solved() == False
    
def test_solved_true():
    game = GuessingGame(10)
    game.guess(10)
    assert game.solved() == True