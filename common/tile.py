from constants import *

class Tile:
    def __init__(self, coord, board, item=None, item_qty=0, ant=None):
        self.x, self.y = coord
        self.board = board
        self.item = item
        self.item_qty = item_qty
        self.ant = ant

    def __str__(self):
        char = " "
        if self.ant != None:
            char = "a"
        elif self.item == "food":
            char = "."
        elif self.item == "rock":
            char = "0"

        return char

    def to_dict(self):
        return {
        }

    def color(self):
        if self.has_ant():
            return (0,244,0)
        if self.has_item():
            return self.item.color()
        else:
            return COLORS['brown']

    def adjacent_tiles(self):
        return self.board.adjacent_tiles((self.x, self.y))

    def tile_from_dir(self, direction):
        return self.board.tile_from_dir(self, direction)

    def is_in_bounds(self):
        return self.board.is_coord_in_bounds((self.x, self.y))

    def has_ant(self):
        return self.ant is not None

    def has_ant(self):
        return self.item is not None
