from random import shuffle

from common.board import Board
from common.ant import Ant
from common.player import Player

class Game:
    def __init__(self, settings, players):
        self.settings = settings
        self.players = players
        self.board = Board(settings["board_height"], settings["board_width"], True)
        self.game_tick = 0
        self.actions = []

        # Initialize ants
        self.ants = []
        for player in self.players:
            tile = self.board.random_empty_tile()
            self.ants.append(Ant(player, tile, "queen"))

    def advance_game(self):
        shuffle(self.ants)
        for ant in self.ants:
            action = ant.player.get_action_for_ant(ant, self.board)
            if action.is_valid_action:
                self.apply_action(action)
                self.actions.append(action)
        self.game_tick += 1

    def apply_action(self, action):
        if action.type == "move":
            # WIP action.ant.move(action.direction)
            # action.ant.energy -= 1
            print("moving " + action.direction)
