class Action: # Lawsuit
    def __init__(self, ant, action_hash):
        self.ant = ant
        self.board = ant.tile.board
        self.type = action_hash["type"]
        self.direction = action_hash["direction"]

    def perform(self):
        if self.type == "move":
            new_tile = self.board.tile_from_dir(self.ant.tile, self.direction)
            # This shouldn't be on the ant
            self.ant.move(self.direction)

    def is_valid(self):
        if self.out_of_bounds():
            return False

        return True

    def out_of_bounds(self):
        new_tile = self.board.tile_from_dir(self.ant.tile, self.direction)

        if new_tile is None:
            return True
