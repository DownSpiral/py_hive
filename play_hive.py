from game.game_engine import GameEngine
from common.game import Game

if __name__ == '__main__':
    game_settings = {
        'food_amount': 10,
        'food_sprawl': 100,
        'food_sources': 50,
        'board_settings': {
            'width': 4,
            'height': 6,
            'wrapping': True,
        },
        'players_settings': [
            # { 'ai': "scripts.ais.right", 'color': "black" },
            # { 'ai': "scripts.ais.left", 'color': "black" },
            # { 'ai': "scripts.ais.up", 'color': "black" },
            # { 'ai': "scripts.ais.down", 'color': "black" },
            # { 'ai': "scripts.ais.random_walk", 'color': "red" },
            # { 'ai': "scripts.ais.random_walk", 'color': "blue" },
            # { 'ai': "scripts.harvester.perform", 'color': "random" },
            # { 'ai': "scripts.harvester.perform", 'color': "random" },
            # { 'ai': "scripts.harvester.perform", 'color': "random" },
            { 'ai': "scripts.harvester.perform", 'color': "random" },
        ]
    }
    display_settings = {
        'width': 800,
        'height': 800,
        'pixels_per_tile': 25,
        'game_speed': 12
    }

    engine = GameEngine(game_settings, display_settings)
    engine.start()

    print('all done')
