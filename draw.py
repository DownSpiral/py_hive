import pygame

def tap_pygame():
    if not pygame.get_init():
        pygame.init()

class Draw:
    def __init__(self, start=False):
        tap_pygame()

        self.width = 800
        self.height = 600

        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit')
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                print('up')

            if event.type == pygame.KEYDOWN:
                print('down')

    def update(self, speed=60):
        pygame.display.update()
        self.clock.tick(speed)
