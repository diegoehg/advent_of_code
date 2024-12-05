import pytest
from cubes import parse_game

@pytest.fixture(params=[("Game 1: 1 blue", 1), ("Game 34: 2 red", 34)], ids=[1, 34])
def ids_lines(request):
    return request.param


def test_parse_game_id(ids_lines):
    game = parse_game(ids_lines[0])
    assert game.id == ids_lines[1]


def test_parse_game_combination():
    game = parse_game("Game 4: 1 red")
    assert game.combinations[0]["red"] == 1
