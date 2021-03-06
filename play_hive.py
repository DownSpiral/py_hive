from game.game_engine import GameEngine
from common.game import Game

if __name__ == '__main__':
    game_settings = {
        'food_amount': 5,
        'food_sprawl': 75,
        'food_sources': 10,
        'board_settings': {
            'width': 50,
            'height': 30,
            'wrapping': True,
        },
        'players_settings': [
            { 'ai': "scripts.harvester.perform", 'color': "blue" },
            { 'ai': "scripts.harvester.perform", 'color': "red" },
        ]
    }
    display_settings = {
        'width': 1400,
        'height': 900,
        'pixels_per_tile': 25,
        'game_speed': 12
    }

    engine = GameEngine(game_settings, display_settings)
    engine.start()

    print('all done')
