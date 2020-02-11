from constants import *

# Base class for all things that can be an item on a tile
# Should all item types have a corresponding Action type?
class Item:
    def __init__(self,**settings):
        self.tile = settings['tile']
        self.settings = settings
        self.name = 'item'

    def color(self):
        return COLORS['black']

    def to_dict(self):
        return {
            'type': self.__class__.__name__.lower()
        }
