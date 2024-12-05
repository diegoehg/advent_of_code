import re

class Game:
    def __init__(self, id, combinations):
        self.id = id
        self.combinations = combinations


def parse_game(line):
    game_pattern = re.compile(r'\d+')
    game_id = game_pattern.match(line.lstrip("Game "))
    id = int(game_id.group())

    semicolon_index = line.find(":")
    print(line[semicolon_index+2:])
    tokens = line[semicolon_index+2:].split(" ")
    print(tokens)
    combination = {}
    combination[tokens[1]] = int(tokens[0])

    return Game(id, [combination])
