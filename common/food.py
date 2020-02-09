from constants import *
from common.item import Item

class Food(Item):
    def __init__(self, **settings):
        self.quantity = settings['quantity']
        super().__init__(**settings)
        self.name = 'food'

    def color(self):
        if self.quantity > 50:
            return FOOD_COLORS['dense']
        elif self.quantity > 20:
            return FOOD_COLORS['medium']
        else:
            return FOOD_COLORS['light']

    def to_dict(self):
        super_attrs = super().to_dict()
        attrs = {
            'type': self.__class__.__name__.lower()
        }
        # Merge parent class to_dict attrs
        return { **super_attrs, **attrs }
