from common.item import Item
class Food(Item):
    def __init__(self, **settings):
        self.quantity = settings['quantity']
        super().__init__(**settings)

    def wat(self):
        print(self.quantity)
        print(self.tile.x, self.tile.y)
        super().wat()
