import pygame

from game.display import Display
from common.game import Game
from common.board import Board

class GameEngine:
    def __init__(self, game_settings, display_settings):
        self.display = Display(display_settings)
        self.game = Game(game_settings)
        self.running = False

    def start(self):
        self.display.render_board(self.game.board)

        self.running = True
        while self.running:
            # Process events
            for event in pygame.event.get():
                self.handle_event(event)

            self.update_game()
            # Eventually, this should take in a list of all tiles that need to rendering, but
            # until we hit performance issues, we'll just render the whole board every update
            self.display.render_updates(self.game.board)

    def stop(self):
        self.running = False

    def update_game(self):
        self.game.advance_game()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()

        if event.type == pygame.KEYUP:
            print('up')

        if event.type == pygame.KEYDOWN:
            print('down')
