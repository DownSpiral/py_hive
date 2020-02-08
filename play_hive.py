from game.game_engine import GameEngine
from common.game import Game

if __name__ == '__main__':
    game_settings = {
        'food_amount': 9,
        'food_sources': 5,
        'board_settings': {
            'width': 50,
            'height': 40,
            'wrapping': True,
        },
        'players_settings': [
            { 'ai': "scripts.line.right", 'color': "random" },
            { 'ai': "scripts.line.left", 'color': "random" },
            { 'ai': "scripts.line.up", 'color': "random" },
            { 'ai': "scripts.line.down", 'color': "random" },
            { 'ai': "scripts.ais.random_walk", 'color': "random" },
            { 'ai': "scripts.ais.random_walk", 'color': "random" },
            { 'ai': "scripts.ais.random_walk", 'color': "random" },
            { 'ai': "scripts.ais.random_walk", 'color': "random" }
        ]
    }
    display_settings = {
        'width': 1200,
        'height': 800,
        'pixels_per_tile': 16,
        'game_speed': 12
    }

    engine = GameEngine(game_settings, display_settings)
    engine.start()

    print('all done')
