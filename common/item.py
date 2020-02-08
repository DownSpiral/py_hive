# Base class for all things that can be an item on a tile
# Should all item types have a corresponding Action type?
class Item:
    def __init__(self,**settings):
        self.tile = settings['tile']
        self.settings = settings

    def wat(self):
        for k, v in self.settings:
            print(f"{k} wat {v}")
