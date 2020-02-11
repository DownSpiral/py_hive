from game.game_engine import GameEngine
from common.game import Game

if __name__ == '__main__':
    game_settings = {
        'food_amount': 5,
        'food_sprawl': 75,
        'food_sources': 10,
        'board_settings': {
            'width': 30,
            'height': 20,
            'wrapping': True,
        },
        'players_settings': [
            { 'ai': "scripts.harvester.perform", 'color': "random" },
            { 'ai': "scripts.harvester.perform", 'color': "random" },
        ]
    }
    display_settings = {
        'width': 1200,
        'height': 900,
        'pixels_per_tile': 16,
        'game_speed': 12
    }

    engine = GameEngine(game_settings, display_settings)
    engine.start()

    print('all done')
