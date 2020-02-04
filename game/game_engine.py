import pygame

from common.board import Board

class GameEngine:
    def __init__(self, game, display):
        self.running = False
        self.game_speed = 4

        self.display = display
        self.game = game

        # What is this clock? Should we use it for our game clock too?
        self.clock = pygame.time.Clock()
        self.updates = []

    def start(self):
        self.running = True

        self.display.render_board(self.game.board)

        while self.running:
            # Process events
            for event in pygame.event.get():
                self.handle_event(event)

            self.update_game()
            self.render_updates()
            self.clock.tick(self.game_speed)

    def stop(self):
        self.running = False

    def update_game(self):
        self.game.advance_game()

    def render_updates(self):
        self.display.render_updates(self.updates)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()

        if event.type == pygame.KEYUP:
            print('up')

        if event.type == pygame.KEYDOWN:
            print('down')
