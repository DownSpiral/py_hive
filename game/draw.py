import pygame

class Draw:
    def __init__(self, start=False):
        if not pygame.get_init():
            pygame.init()

        self.width = 800
        self.height = 600

        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def update(self, speed=60):
        pygame.display.update()
        self.clock.tick(speed)

    def square(self, s):
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(1, 1, s, s))
        pygame.display.update()
