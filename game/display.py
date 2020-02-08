import pygame

class Display:
    def __init__(self, display_settings):
        if not pygame.get_init():
            pygame.init()

        self.ppt = display_settings['pixels_per_tile']
        self.width = display_settings['display_width']
        self.height = display_settings['display_height']

        self.display = pygame.display.set_mode((self.width, self.height))

    def render_updates(self, updates):
        # Figure out how to render updates
        pygame.display.flip()

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
