from game.game_engine import GameEngine
from common.player import Player

if __name__ == '__main__':
    game_settings = { "height": 4, "width": 4 }
    players = [
        Player(1, "scripts.foo.bar", "red"),
        Player(2, "scripts.bar.baz", "blue")
    ]
    engine = GameEngine(game_settings, players)
    engine.start()
    print('all done')
