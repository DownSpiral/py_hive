def random_walk(ant_data):
    return { 'type': 'move', 'direction': choice(['left', 'right', 'up', 'down']) }

def right(ant_data):
    return { "type": "move", "direction": "right" }

def left(ant_data):
    return { "type": "move", "direction": "left" }

def up(ant_data):
    return { "type": "move", "direction": "up" }

def down(ant_data):
    return { "type": "move", "direction": "down" }
