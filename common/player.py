import constants
from importlib import import_module

from common.action import Action

class Player:
    def __init__(self, **settings):
        self.id = settings['player_id']
        self.color_name = settings['color']
        file_name, func = settings['ai'].rsplit('.', 1)
        module = import_module(file_name)
        self.ai_func = getattr(module, func)

    def get_action_for_ant(self, ant, board):
        ant_data = ant.to_dict().update({
            'current_tile': ant.tile.to_dict,
            'adjacent_tiles': [
                t.to_dict for t in board.adjacent_tiles((ant.tile.x, ant.tile.y))
            ]
        })
        return Action(ant, self.ai_func(ant_data))

    def color(self):
        # For random colors
        if self.color_name is 'random':
            return constants.random_color()

        return constants.COLORS[self.color_name]
