from copy import copy
from common.food import Food

class Action:
    def __init__(self, ant, action_hash):
        self.ant = ant
        self.board = ant.tile.board
        self.type = action_hash["type"]

        if 'direction' in action_hash:
            self.direction = action_hash["direction"]
            if self.type == 'pick_up':
                self.item = self.ant.tile.tile_from_dir(self.direction).item
        if 'quantity' in action_hash:
            self.quantity = action_hash['quantity']

    def perform(self):
        if self.type == "move":
            new_tile = self.board.tile_from_dir(self.ant.tile, self.direction)
            if not self.is_valid_move(new_tile):
                return False

            self.ant.move_counts[self.direction] += 1
            new_tile.ant = self.ant
            self.ant.tile.ant = None
            self.ant.tile = new_tile
            self.ant.subtract_energy(1)

        if self.type == 'pick_up':
            if not self.is_valid_pick_up():
                return False
            if self.item.quantity > self.quantity:
                new_item = copy(self.item)
                new_item.quantity -= self.quantity
                self.item.quantity = self.quantity
            if self.ant.item:
                self.ant.item.quantity += self.item.quantity
            else:
                self.ant.item = self.item
                self.item.tile = None
            self.ant.subtract_energy(1)

        if self.type == 'lay_egg':
            if not self.is_valid_lay_egg():
                return False

            print('laying an egg')
            self.ant.subtract_energy(1)

        if self.type == 'eat':
            if not self.is_valid_eat():
                return False

            print('eating!')

            self.ant.subtract_food(1)
            self.ant.add_energy(25)

        return True

    def is_valid_move(self, tile):
        if self.tile_out_of_bounds(tile):
            return False

        if tile.has_ant():
            return False

        return True

    def is_valid_pick_up(self):
        if type(self.quantity) == int and (self.quantity < 1 or self.quantity > self.ant.stats['capacity']):
            return False
        if self.ant.has_item():
            if type(self.ant.item) is not type(self.item):
                return False
            if self.ant.item.quantity + self.quantity > self.ant.stats['capacity']:
                return False
        if not self.item in [self.ant.tile.item] + [t.item for t in self.ant.tile.adjacent_tiles()]:
            return False

        return True

    def is_valid_lay_egg(self):
        if not self.ant.is_queen():
            return False

        if self.ant.current_energy() < Ant.WORKER_COST:
            return False

        tile_for_egg = self.ant.tile.tile_from_dir(self.direction)
        if tile_for_egg.has_item():
            return False

    def is_valid_eat(self):
        print('valid eat?')
        if not type(self.ant.item) == Food:
            print('naw type')
            return False
        if self.ant.item.quantity <= 0:
            print('naw quant')
            return False
        return True

    def tile_out_of_bounds(self, tile):
        return tile is None
