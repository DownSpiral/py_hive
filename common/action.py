class Action: # Lawsuit
    def __init__(self, ant, action_hash):
        self.ant = ant
        self.type = action_hash["type"]
        self.direction = action_hash["direction"]

    def is_valid(self):
        if action.type not in ('move'):
          return False
        if action.direction and action.direction in ('up', 'down', 'left', 'right'):
          return False

        return True

    def perform(self):
        if action.type == "move":
            # WIP action.ant.move(action.direction)
            # action.ant.energy -= 1
            print("moving " + action.direction)
