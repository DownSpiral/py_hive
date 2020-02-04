import pygame

from common.game import Game
from common.board import Board

class GameEngine:
    def __init__(self, game_settings, players):
        if not pygame.get_init():
            pygame.init()

        # pixels per tile
        self.ppt = 64

        self.running = False
        self.game_speed = 4

        self.width = 1200
        self.height = 800
        self.display = pygame.display.set_mode((self.width, self.height))
        self.game = Game(game_settings, players)

        # What is this clock? Should we use it for our game clock too?
        self.clock = pygame.time.Clock()

    def start(self):
        self.running = True

        self.render_board()

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
        # Figure out how to render a list of updates
        pygame.display.flip()


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()

        if event.type == pygame.KEYUP:
            print('up')

        if event.type == pygame.KEYDOWN:
            print('down')

    def render_board(self):
        self.display.fill((255,255,255))
        for row in self.game.board.tiles:
            for tile in row:
                self.render_tile(tile)

    def render_tile(self, tile):
        (x, y) = (tile.coord.x, tile.coord.y)
        (rx, ry) = (self.ppt * x, self.ppt * y)

        self.square(rx, ry, self.ppt, tile.color())

    def render_square(self, x, y, length, color):
        pygame.draw.rect(self.display, color, pygame.Rect(x, y, length, length))
