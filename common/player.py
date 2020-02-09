import constants
from importlib import import_module
from random import choice

from common.action import Action

class Player:
    def __init__(self, **settings):
        self.id = settings['player_id']
        self.color_name = settings['color']
        file_name, func = settings['ai'].rsplit('.', 1)
        module = import_module(file_name)
        self.ai_func = getattr(module, func)

        # For random colors
        if self.color_name is 'random':
            self.color_name = choice(list(constants.COLORS.keys()))


    def get_action_for_ant(self, ant, board):
        ant_data = ant.to_dict()
        tile_data = {
            'current_tile': ant.tile.to_dict(),
            'adjacent_tiles': { direction: board.adjacent_tiles_dict(ant.tile)[direction].to_dict() for direction in board.adjacent_tiles_dict(ant.tile).keys() }
        }
        return Action(ant, self.ai_func({ **ant_data, **tile_data }))

    def color(self):
        return constants.COLORS[self.color_name]
