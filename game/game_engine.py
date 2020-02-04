import pygame

from common.board import Board

class Game:
    def __init__(self):
        self.turn = 0
        self.board = Board(10,10)

    def update(self):
        self.turn += 1
        print(self.turn)

class GameEngine:
    def __init__(self):
        if not pygame.get_init():
            pygame.init()

        # pixels per tile
        self.ppt = 64

        self.running = False
        self.game_speed = 4

        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode((self.width, self.height))
        self.game = Game()

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
        self.game.update()

    def render_updates(self):
        # Figure out how to render a list of updates
        pygame.display.flip()


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()

        if event.type == pygame.KEYUP:
            print('up')

        if event.type == pygame.KEYDOWN:
            self.square(5)
            print('down')

    def square(self, s):
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(1, 1, s, s))

    def render_board(self):
        self.display.fill((255,255,255))
        for row in self.game.board.tiles:
            for tile in row:
                self.render_tile(tile)

    def render_tile(self, tile):
        (x, y) = (tile.coord.x, tile.coord.y)
        (rx, ry) = (self.ppt * x, self.ppt * y)
        pygame.draw.rect(self.display, tile.color(), pygame.Rect(rx, ry, self.ppt, self.ppt))