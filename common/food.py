from constants import *
from common.item import Item

class Food(Item):
    def __init__(self, **settings):
        self.quantity = settings['quantity']
        super().__init__(**settings)

    def color(self):
        return COLORS['green']

    def to_dict(self):
        super_attrs = super().to_dict()
        attrs = {
            'type': self.__class__.__name__.lower()
        }
        # Merge parent class to_dict attrs
        return { **super_attrs, **attrs }
