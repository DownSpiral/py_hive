from tile import Tile
from coord import Coord

class Board:
  def __init__(self, height, width, wrapping=False):
    if height <= 0 or width <= 0:
      raise "Must have height and width > 1"
    self.height = height
    self.width = width
    self.wrapping = wrapping
    self.board = [None] * self.height
    for i in range(self.height):
      self.board[i] = [None] * self.width
      for j in range(self.width):
        self.board[i][j] = Tile(Coord(j, i), "food", 1)

  def __str__(self):
    return '\n'.join(' '.join(map(str, sl)) for sl in self.board)

  def get_tile(self, x, y):
    return self.board[y][x]

  def surrounding_tiles(self, coord):
    tiles = []
    # Left
    if coord.x == 0 and self.wrapping:
      tiles.append(self.get_tile(self.width - 1, coord.y))
    elif coord.x != 0:
      tiles.append(self.get_tile(coord.x - 1, coord.y))

    # Right
    if coord.x == self.width and self.wrapping:
      tiles.append(self.get_tile(0, coord.y))
    elif coord.x < self.width:
      tiles.append(self.get_tile(coord.x + 1, coord.y))

    # Down
    if coord.y == 0 and self.wrapping:
      tiles.append(self.get_tile(coord.x, self.height - 1))
    elif coord.y != 0:
      tiles.append(self.get_tile(coord.x, coord.y - 1))

    # Up
    if coord.y == self.height and self.wrapping:
      tiles.append(self.get_tile(coord.x, 0))
    elif coord.y < self.height:
      tiles.append(self.get_tile(coord.x, coord.y + 1))

    return tiles
