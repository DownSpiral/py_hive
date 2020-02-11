from random import choice

def is_worker(ant_type):
    return ant_type is 'worker'

def is_queen(ant_type):
    return ant_type is 'queen'

def adjacent_food_tiles(tiles):
    return { d: tile for d, tile in tiles.items() if tile['item'] is not None and tile['item']['type'] == 'food' }

def adjacent_items(adjacent_tiles):
    return [tile['item'] for tile in adjacent_tiles.values()]

# return true if there is at least one free tile
def has_empty_tile(tiles):
    any([True for item in adjacent_items(tiles) if item is None])

def can_lay_egg(ant_data):
    print(ant_data['energy'], ant_data['energy'] > 25 and has_empty_tile(ant_data['adjacent_tiles']))
    return ant_data['energy'] > 25 and has_empty_tile(ant_data['adjacent_tiles'])

def has_food(ant_data):
    return 'item' in ant_data and ant_data['item'] == 'food' and ant_data['item_qty'] > 0

def should_eat(ant_data):
    return ant_data['energy'] < 15 and has_food(ant_data)

def should_pick_up(ant_data):
    if ant_data['item'] is None:
        return True
    elif ant_data['item'] == 'food' and ant_data['item_qty'] < ant_data['capacity']:
        return True

    return False

def perform(ant_data):
    adjacent_tiles = ant_data['adjacent_tiles']
    food_tiles = adjacent_food_tiles(adjacent_tiles)

    # There aren't workers yet
    if is_queen(ant_data['type']):
        # Eat if it's running low on energy
        if should_eat(ant_data):
            print('eating')
            return { 'type': 'eat' }

        # Eat if it's running low on energy
        if can_lay_egg(ant_data):
            print('laying')
            return {
                'type': 'lay_egg',
                'direction': choice(adjacent_tiles.keys()),

            }
        if len(food_tiles) is not 0 and should_pick_up(ant_data):
            return {
                'type': 'pick_up',
                'direction': choice(list(food_tiles.keys())),
                'quantity': ant_data['capacity']
            }

    return {
        'type': 'move',
        'direction': choice(['left', 'right', 'up', 'down'])
    }
