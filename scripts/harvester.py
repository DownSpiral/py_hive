from random import choice

def is_worker(ant_type):
    return ant_type is 'worker'

def is_queen(ant_type):
    return ant_type is 'queen'

def has_item(tile):
    if tile['item'] is not None:
        return True

def has_food(tile):
    if not has_item(tile):
        return False

    return tile['item']['type'] == 'food'

def adjacent_food_tiles(adjacent_tiles):
    return { direction: adjacent_tiles[direction] for direction in adjacent_tiles.keys() if has_food(adjacent_tiles[direction]) }

def perform(ant_data):
    food_tiles = adjacent_food_tiles(ant_data['adjacent_tiles'])

    # There aren't workers yet
    if is_queen(ant_data['type']):
        if len(food_tiles) is not 0:
            return { 'type': 'pick_up', 'direction': choice(list(food_tiles.keys())), 'quantity': ant_data['capacity'] }

    return { 'type': 'move', 'direction': choice(['left', 'right', 'up', 'down']) }
