from game.game_engine import GameEngine
from game.display import Display
from common.player import Player
from common.game import Game

if __name__ == '__main__':
    game_settings = { "board_height": 10, "board_width": 10 }
    players = [
        Player(1, "scripts.foo.bar", "red"),
        Player(2, "scripts.bar.baz", "blue")
    ]
    game = Game(game_settings, players)

    display_settings = { "display_height": 800, "display_width": 1200 }
    display = Display(display_settings)

    engine = GameEngine(game, display)
    engine.start()

    print('all done')
