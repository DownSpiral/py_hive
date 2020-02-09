class Action: # Lawsuit
    def __init__(self, ant, action_hash):
        self.ant = ant
        self.board = ant.tile.board
        self.type = action_hash["type"]
        self.direction = action_hash["direction"]

    def perform(self):
        if self.type == "move":
            new_tile = self.board.tile_from_dir(self.ant.tile, self.direction)
            if not self.is_valid(new_tile):
                return False

            self.ant.move_counts[self.direction] += 1
            new_tile.ant = self.ant
            self.ant.tile.ant = None
            self.ant.tile = new_tile

        if self.type == 'gather':
            print(f'player {self.ant.player.id} gathering')

        return True

    def is_valid(self, tile):
        if self.tile_out_of_bounds(tile):
            return False

        if tile.has_ant():
            return False

        return True

    def tile_out_of_bounds(self, tile):
        return tile is None
