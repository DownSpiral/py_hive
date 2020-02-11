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
    return { d: adjacent_tiles[d] for d in adjacent_tiles.keys() if has_food(adjacent_tiles[d]) }

def adjacent_items(adjacent_tiles):
    return [tile.item for tile in adjacent_tiles.values()]

# return true if there is at least one free tile
def has_empty_tile(tiles):
    any([True for item in adjacent_items(tiles) if item is None)

def can_lay_egg(ant_data):
    ant_data['energy'] > 50 and has_empty_tile(ant_data['adjacent_tiles'])

def should_eat(ant_data):
    return ant_data['energy'] < 15 and ant_data['item_qty'] > 0

def perform(ant_data):
    adjacent_tiles = ant_data['adjacent_tiles']
    food_tiles = adjacent_food_tiles(adjacent_tiles)

    # There aren't workers yet
    if is_queen(ant_data['type']):
        # Eat if it's running low on energy
        if should_eat(ant_data):
            return { 'type': 'eat' }

        # Eat if it's running low on energy
        if can_lay_egg(ant_data):
            return {
                'type': 'lay_egg',
                'direction': choice(adjacent_tiles.keys()),

            }
        if len(food_tiles) is not 0:
            return {
                'type': 'pick_up',
                'direction': choice(list(food_tiles.keys())),
                'quantity': ant_data['stats']['capacity']
            }

    return {
        'type': 'move',
        'direction': choice(['left', 'right', 'up', 'down'])
    }
