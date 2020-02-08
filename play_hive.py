from game.game_engine import GameEngine
from common.game import Game

if __name__ == '__main__':
    game_settings = {
        'food_amount': 50,
        'food_sources': 12,
        'board_settings': {
            'width': 120,
            'height': 90,
            'wrapping': True,
        },
        'players_settings': [
            { 'ai': "scripts.ais.right", 'color': "black" },
            { 'ai': "scripts.ais.left", 'color': "black" },
            { 'ai': "scripts.ais.up", 'color': "black" },
            { 'ai': "scripts.ais.down", 'color': "black" },
            { 'ai': "scripts.ais.random_walk", 'color': "red" },
            { 'ai': "scripts.ais.random_walk", 'color': "blue" },
            { 'ai': "scripts.harvester.perform", 'color': "random" },
            { 'ai': "scripts.harvester.perform", 'color': "random" },
            { 'ai': "scripts.harvester.perform", 'color': "random" },
            { 'ai': "scripts.harvester.perform", 'color': "random" },
        ]
    }
    display_settings = {
        'width': 1200,
        'height': 800,
        'pixels_per_tile': 8,
        'game_speed': 12
    }

    engine = GameEngine(game_settings, display_settings)
    engine.start()

    print('all done')
