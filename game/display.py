import pygame

class Display:
    def __init__(self, settings):
        if not pygame.get_init():
            pygame.init()

        self.width = settings['width']
        self.height = settings['height']
        self.ppt = settings['pixels_per_tile']
        self.game_speed = settings['game_speed']

        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.width, self.height))

    def render_updates(self, board):
        # Figure out how to render updates
        self.render_board(board)
        self.clock.tick(self.game_speed)

    def render_board(self, board):
        pygame.display.flip()
        self.display.fill((255,255,255))
        for row in board.tiles:
            for tile in row:
                self.render_tile(tile)

    def render_tile(self, tile):
        (pixel_width, pixel_height) = (self.ppt * tile.x, self.ppt * tile.y)
        self.render_square(pixel_width, pixel_height, tile.color())

    def render_square(self, x, y, color):
        pygame.draw.rect(self.display, color, pygame.Rect(x, y, self.ppt, self.ppt))
