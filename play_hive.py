from game.game_engine import GameEngine
from common.game import Game

if __name__ == '__main__':
    player_settings = [
        { 'ai': "scripts.foo.bar", 'color': "red" },
        { 'ai': "scripts.bar.baz", 'color': "blue" },
        { 'ai': "scripts.bar.baz", 'color': "green" }
    ]
    game_settings = {
        'board_width': 30,
        'board_height': 20,
        'wrapping': True,
        'player_settings': player_settings
    }
    display_settings = {
        'display_width': 1200,
        'display_height': 800,
        'pixels_per_tile': 16
    }

    #engine = GameEngine(game_settings, display_settings)
    #engine.start()

    g = Game(game_settings)
    print(g.board)
    print('all done')
