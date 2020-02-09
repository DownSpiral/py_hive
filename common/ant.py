import copy

class Ant:
    def __init__(self, player, tile, type):
        self.type = type
        self.player = player
        self.tile = tile
        if tile.ant == None:
          tile.ant = self
        self.move_counts = {
            "up": 0,
            "down": 0,
            "left": 0,
            "right": 0
        }
        self.item = None
        self.capacity = 10

    def to_dict(self):
        return copy.deepcopy({
            "type": self.type,
            "player_id": self.player.id,
            "move_counts": self.move_counts,
            "item": self.item,
            "capacity": self.capacity
        })

    def color(self):
        return self.player.color()

    def has_item(self):
        return self.item is not None
