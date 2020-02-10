import copy

class Ant:
    def __init__(self, **settings):
        self.type = settings['type']
        self.player = settings['player']
        self.tile = settings['tile']

        self.item = None
        if 'item' in settings:
            self.item = settings['item']

        if self.tile.ant == None:
            self.tile.ant = self

        self.move_counts = {
            "up": 0,
            "down": 0,
            "left": 0,
            "right": 0
        }

        self.stats = {
            'capacity': 10,
            'max_health': 100,
            'max_energy': 1000,
            'health':  100,
            'energy':  1000,
        }


    # attrs returned {
    #     type:        queen, worker,
    #     player_id:   the ant's owner,
    #     move_counts: left, right, up, down,
    #     stats:       defaults and current stats,
    #     item?:       
    #     item_qty?:
    # }
    def to_dict(self):
        d = {
            "type": self.type,
            "player_id": self.player.id,
            "move_counts": self.move_counts,
            'stats': self.stats
        }
        if self.item is not None:
            d["item"] = self.item.name
            d["item_qty"] = self.item.quantity
        return copy.deepcopy(d)

    def color(self):
        return self.player.color()

    def has_item(self):
        return self.item is not None
