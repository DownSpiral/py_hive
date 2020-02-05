import pygame

class Display:
    def __init__(self, display_settings):
        if not pygame.get_init():
            pygame.init()

        # pixels per tile
        self.ppt = 64
        self.width = display_settings['display_width']
        self.height = display_settings['display_height']

        self.display = pygame.display.set_mode((self.width, self.height))

    def render_updates(self, updates):
        # Figure out how to render updates
        pygame.display.flip()

    def render_board(self, board):
        self.display.fill((255,255,255))
        for row in board.tiles:
            for tile in row:
                self.render_tile(tile)

    def render_tile(self, tile):
        (x, y) = (tile.coord.x, tile.coord.y)
        (rx, ry) = (self.ppt * x, self.ppt * y)

        self.render_square(rx, ry, self.ppt, tile.color())

    def render_square(self, x, y, length, color):
        pygame.draw.rect(self.display, color, pygame.Rect(x, y, length, length))
