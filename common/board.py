from common.tile import Tile
from common.coord import Coord
import random

class Board:
    def __init__(self, height, width, wrapping=False):
        if height <= 0 or width <= 0:
            raise "Must have height and width > 1"
        self.height = height
        self.width = width
        self.wrapping = wrapping
        self.tiles = [None] * self.height
        for i in range(self.height):
            self.tiles[i] = [None] * self.width
            for j in range(self.width):
                self.tiles[i][j] = Tile(Coord(j, i), self, "food", 1)

    def __str__(self):
        return '\n'.join(' '.join(map(str, sl)) for sl in self.tiles)

    def get_tile(self, x, y):
        # Within an action, we need to ask the board if the movement is in bounds
        # We can't get the tile and then ask because it will error out of bounds
        # on the array. What's a good way around this? Here I just return None on
        # this method, but it feels wrong.
        if not self.is_coord_in_bounds(Coord(x, y)):
            return None

        return self.tiles[y][x]

    def tile_from_dir(self, tile, direction):
        (x, y) = (tile.coord.x, tile.coord.y)
        return {
            'left': self.get_tile(x - 1, y),
            'right': self.get_tile(x + 1, y),
            'up': self.get_tile(x, y - 1),
            'down': self.get_tile(x, y + 1),
        }[direction]

    def adjacent_tiles(self, coord):
        tiles = []
        # Left
        if coord.x == 0 and self.wrapping:
            tiles.append(self.get_tile(self.width - 1, coord.y))
        elif coord.x != 0:
            tiles.append(self.get_tile(coord.x - 1, coord.y))

        # Right
        if coord.x == self.width - 1 and self.wrapping:
            tiles.append(self.get_tile(0, coord.y))
        elif coord.x < self.width - 1:
            tiles.append(self.get_tile(coord.x + 1, coord.y))

        # Down
        if coord.y == 0 and self.wrapping:
            tiles.append(self.get_tile(coord.x, self.height - 1))
        elif coord.y != 0:
            tiles.append(self.get_tile(coord.x, coord.y - 1))

        # Up
        if coord.y == self.height - 1 and self.wrapping:
            tiles.append(self.get_tile(coord.x, 0))
        elif coord.y < self.height - 1:
            tiles.append(self.get_tile(coord.x, coord.y + 1))

        return tiles

    def flat_tiles(self):
        return [tile for row in self.tiles for tile in row]

    def random_empty_tile(self):
        tiles = self.flat_tiles()
        random.shuffle(tiles)
        return next(tile for tile in tiles if tile.ant == None)

    def is_coord_in_bounds(self, coord):
        return coord.x >= 0 and coord.x < self.width and coord.y >= 0 and coord.y < self.height
