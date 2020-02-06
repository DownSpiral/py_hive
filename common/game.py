from random import shuffle

from common.board import Board
from common.ant import Ant
from common.player import Player

class Game:
    def __init__(self, settings):
        self.settings = settings
        self.board = Board(
            settings['board_height'],
            settings['board_width'],
            settings['wrapping']
        )
        self.game_tick = 0
        self.actions = []

        self.players = []
        self.ants = []
        for i, player in enumerate(settings['player_settings']):
            # Initialize players
            player = Player(i, player['ai'], player['color'])
            self.players.append(player)

            # Initialize ants
            tile = self.board.random_empty_tile()
            self.ants.append(Ant(player, tile, "queen"))

    def advance_game(self):
        shuffle(self.ants)
        for ant in self.ants:
            action = ant.player.get_action_for_ant(ant, self.board)
            # Perform the action. If it succeeds, append it to actions
            if action.perform():
                # This will get big pretty fast if we don't flush it
                self.actions.append(action)
        self.game_tick += 1
