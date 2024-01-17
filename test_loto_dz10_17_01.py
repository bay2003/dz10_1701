from random import randint, sample
from loto import Keg, Card, Game, generate_unique_numbers
# test_loto.py

def test_keg_creation():
    keg = Keg()
    assert 1 <= keg.num <= 90

def test_keg_str_representation():
    keg = Keg()
    assert isinstance(str(keg), str)

def test_card_creation():
    card = Card()
    assert isinstance(card, Card)

def test_card_str_representation():
    card = Card()
    assert isinstance(str(card), str)

def test_card_contains():
    card = Card()
    assert 1 in card
    assert 91 not in card

def test_card_cross_num():
    card = Card()
    num = 1
    card.cross_num(num)
    assert num not in card
    num = 91
    try:
        card.cross_num(num)
    except ValueError as e:
        assert str(num) in str(e)

def test_card_closed():
    card = Card()
    assert not card.closed()
    for num in range(1, 91):
        card.cross_num(num)
    assert card.closed()

def test_game_creation():
    game = Game(2)
    assert len(game._Game__player_cards) == 2
    assert len(game._Game__compcards) == 2
    assert len(game._Game__kegs) == 90

def test_game_play_round():
    game = Game(2)
    winner, round_result = game.play_round()
    assert winner in [-1, 0, 1]
    assert isinstance(round_result, str)

def test_generate_unique_numbers():
    count = 10
    minbound = 1
    maxbound = 20
    unique_numbers = generate_unique_numbers(count, minbound, maxbound)
    assert isinstance(unique_numbers, list)
    assert len(unique_numbers) == count
    assert all(minbound <= num <= maxbound for num in unique_numbers)
    assert len(set(unique_numbers)) == count


