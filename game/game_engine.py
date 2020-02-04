import pygame

from common.board import Board

class Game:
    def __init__(self):
        self.turn = 0

    def update(self):
        self.turn += 1
        print(self.turn)

class GameEngine:
    def __init__(self):
        if not pygame.get_init():
            pygame.init()
        self.running = False
        self.game_speed = 1
        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode((self.width, self.height))
        self.game = Game()

        # What is this clock? Should we use it for our game clock too?
        self.clock = pygame.time.Clock()

    def start(self):
        self.running = True

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
