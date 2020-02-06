from random import shuffle

from common.board import Board
from common.ant import Ant
from common.player import Player

class Game:
    def __init__(self, settings):
        self.settings = settings
        self.board = Board(settings['board_height'], settings['board_width'], True)
        self.game_tick = 0
        self.actions = []

        # Initialize players
        self.players = []
        for i, player in enumerate(settings['player_settings']):
            self.players.append(Player(i, player['ai'], player['color']))

        # Initialize ants
        self.ants = []
        for player in self.players:
            tile = self.board.random_empty_tile()
            self.ants.append(Ant(player, tile, "queen"))

    def advance_game(self):
        shuffle(self.ants)
        for ant in self.ants:
            action = ant.player.get_action_for_ant(ant, self.board)
            if action.is_valid():
                action.perform()
                self.actions.append(action)
        self.game_tick += 1
