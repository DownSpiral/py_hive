from importlib import import_module

from common.action import Action

class Player:
    def __init__(self, id, ai_module_name, color):
        self.id = id
        self.ai_module_name = ai_module_name
        self.color = color
        file, func = ai_module_name.rsplit('.', 1)
        mod = import_module(file)
        self.ai_func = getattr(mod, func)

    def get_action_for_ant(self, ant, board):
        ant_data = ant.to_dict().update({
            'current_tile': ant.tile.to_dict,
            'adjacent_tiles': [
                t.to_dict for t in board.adjacent_tiles((ant.tile.x, ant.tile.y))
            ]
        })
        return Action(ant, self.ai_func(ant_data))
