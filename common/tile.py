from common.food import Food

class Tile:
    def __init__(self, coord, board, item=None, ant=None):
        self.x, self.y = coord
        self.board = board
        self.item = item
        self.ant = ant

    def __str__(self):
        char = " "
        if self.ant != None:
            char = "a"
        elif type(self.item) is Food:
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
        return self.board.adjacent_tiles((self.x, self.y))

    def tile_from_dir(self, direction):
        return self.board.tile_from_dir(self, direction)

    def is_in_bounds(self):
        return self.board.is_coord_in_bounds((self.x, self.y))

    def has_ant(self):
        return self.ant is not None

    def has_item(self):
        return self.item is not None

    def add_item(self, item):
        self.item = item
