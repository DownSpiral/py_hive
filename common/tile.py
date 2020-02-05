from common.coord import Coord

class Tile:
    def __init__(self, coord, board, item=None, item_qty=0, ant=None):
        self.coord = coord
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
        if self.ant is not None:
            return self.ant.color()
        else:
            return (150, 75, 0)

    def adjacent_tiles(self):
        return self.board.adjacent_tiles(self.coord)

    def tile_from_dir(self, direction):
        return self.board.tile_from_dir(self, direction)
