from random import shuffle
from random import random
from random import choice
from math import ceil

from common.board import Board
from common.ant import Ant
from common.player import Player
from common.food import Food

class Game:
    def __init__(self, settings):
        self.board = Board(**settings['board_settings'])
        self.game_tick = 0
        self.actions = []

        self.players = []
        self.ants = []
        for i, player_settings in enumerate(settings['players_settings']):
            # Initialize players
            player = Player(player_id = i, **player_settings)
            self.players.append(player)

            # Initialize ants
            tile = self.board.random_empty_tile()
            self.ants.append(Ant(player, tile, "queen"))

        # Initialize food
        amt = settings['food_amount']
        num_sources = settings['food_sources']
        sprawl = settings['food_sprawl']
        tiles = self.board.flat_tiles()
        shuffle(tiles)
        for t in tiles[0:num_sources]:
            self.gen_food(t, amt, sprawl)

    def gen_food(self, tile, amt, itr):
        if itr is not 0:
            if type(tile.item) is Food:
                tile.item.quantity += amt
            elif tile.item is None:
                tile.add_item(Food(tile = tile, quantity = amt))

            nt = choice(tile.adjacent_tiles())
            self.gen_food(nt, amt, itr - 1)


    def advance_game(self):
        shuffle(self.ants)
        for ant in self.ants:
            action = ant.player.get_action_for_ant(ant, self.board)
            # Perform the action. If it succeeds, append it to actions
            if action.perform():
                # This will get big pretty fast if we don't flush it
                self.actions.append(action)
        self.game_tick += 1

