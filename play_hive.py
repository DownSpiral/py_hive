# import pygame
# from game.game_engine import GameEngine
from common.game import Game
from common.player import Player

if __name__ == '__main__':
  # game = GameEngine()
  # game.start()
  # print('all done')

    g = Game({ "height": 10, "width": 10 }, [Player(1, "scripts.foo.bar", "red"), Player(2, "scripts.bar.baz", "blue")])
    print(g.board)
    g.advance_game()
    print(g.board)
