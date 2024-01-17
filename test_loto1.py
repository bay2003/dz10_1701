import pytest
from loto01 import Game, PlayerHuman, PlayerComp

def test_player_comp_creation():
    player = PlayerComp()
    assert player.name is not None

def test_player_human_creation():
    player = PlayerHuman()
    assert player.name is not None

def test_game_creation():
    game = Game()
    assert game is not None

def test_game_single_player_human_vs_comp():
    game = Game()
    game.player1 = PlayerHuman()
    game.player2 = PlayerComp()
    game.start()
    assert game.player1 is not None
    assert game.player2 is not None

def test_game_two_players():
    game = Game()
    game.player1 = PlayerHuman()
    game.player2 = PlayerHuman()
    game.start()
    assert game.player1 is not None
    assert game.player2 is not None

def test_game_two_comps():
    game = Game()
    game.player1 = PlayerComp()
    game.player2 = PlayerComp()
    game.start()
    assert game.player1 is not None
    assert game.player2 is not None

if __name__ == '__main__':
    pytest.main()
