from game.game_engine import GameEngine
from common.player import Player

if __name__ == '__main__':
    players = [
        Player(1, "scripts.foo.bar", "red"),
        Player(2, "scripts.bar.baz", "blue")
    ]
    game_settings = {
        "board_width": 10,
        "board_height": 10,
        "players": players
    }
    display_settings = { "display_width": 1200, "display_height": 800}
    engine = GameEngine(game_settings, display_settings)
    engine.start()
    print('all done')
