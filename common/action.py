from copy import deepcopy
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

        if self.type == 'pick_up':
            if not self.is_valid_pick_up():
                return False
            if self.item.quantity > self.quantity:
                new_item = deepcopy(self.item)
                new_item.quantity -= self.quantity
                self.item.quantity = self.quantity
            if self.ant.item:
                self.ant.item.quantity += self.item.quantity
            else:
                self.ant.item = self.item
                self.item.tile = None

        return True

    def is_valid_move(self, tile):
        if self.tile_out_of_bounds(tile):
            return False

        if tile.has_ant():
            return False

        return True

    def is_valid_pick_up(self):
        if type(self.quantity) == int and (self.quantity < 1 or self.quantity > self.ant.capacity):
            return False
        if self.ant.has_item():
            if type(self.ant.item) is not type(self.item):
                return False
            if self.ant.item.quantity + self.quantity > self.ant.capacity:
                return False
        if not self.item in [self.ant.tile.item] + [t.item for t in self.ant.tile.adjacent_tiles()]:
            return False

        return True

    def tile_out_of_bounds(self, tile):
        return tile is None
