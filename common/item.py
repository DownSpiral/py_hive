from constants import *

# Base class for all things that can be an item on a tile
# Should all item types have a corresponding Action type?
class Item:
    def __init(self, tile, **settings):
        self.tile = tile
        self.settings = settings

    def wat(self):
        for k, v in self.settings:
            print(f"{k} wat {v}")

    def color(self):
        return COLORS['black']
