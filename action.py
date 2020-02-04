class Action: # Lawsuit
    def __init__(self, ant, action_hash):
        self.ant = ant
        self.type = action_hash["type"]
        self.direction = action_hash["direction"]

    def is_valid_action(self):
        if action.type not in ('move'):
          return False
        if action.direction and action.direction in ('up', 'down', 'left', 'right'):
          return False

        return True
