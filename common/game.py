from random import shuffle
from random import random
from math import ceil

from common.board import Board
from common.ant import Ant
from common.player import Player
from common.food import Food

import pdb

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
        tiles = self.board.flat_tiles()
        shuffle(tiles)
        for t in tiles[0:num_sources]:
            self.gen_food(t, amt, ["up", "down", "right", "left"], 5, 0.7)

    def gen_food(self, tile, amt, directions, itr, itr_decay):
        if itr is not 0 and amt is not 0:
            if not tile.has_item():
                tile.add_item(Food(tile = tile, quantity = amt))

            new_itr = itr - (1 if random() < itr_decay else 0)
            new_amt = ceil(amt * (new_itr/itr))
            if len(directions) > 1:
                new_dir_count = len(directions) - (1 if random() < itr_decay else 0)
            else:
                new_dir_count = 1

            new_dirs = directions
            shuffle(new_dirs)
            new_dirs = new_dirs[0:new_dir_count]

            tiles = [tile.board.tile_from_dir(tile, direction) for direction in new_dirs]
            tiles = [t for t in tiles if not t.has_item()]
            for nt in tiles:
                self.gen_food(nt, amt, directions, new_itr, itr_decay)


    def advance_game(self):
        shuffle(self.ants)
        for ant in self.ants:
            action = ant.player.get_action_for_ant(ant, self.board)
            # Perform the action. If it succeeds, append it to actions
            if action.perform():
                # This will get big pretty fast if we don't flush it
                self.actions.append(action)
        self.game_tick += 1

