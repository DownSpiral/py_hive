from coord import Coord

class Tile:
  def __init__(self, coord, item=None, item_qty=0, ant=None):
    self.coord = coord
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
