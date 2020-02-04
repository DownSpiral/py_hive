import pygame
from draw import Draw

GAME_SPEED = 60

if __name__ == '__main__':
    draw = Draw()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit')
                run = False

            if event.type == pygame.KEYUP:
                print('up')

            if event.type == pygame.KEYDOWN:
                draw.square(5)
                print('down')



        draw.update(GAME_SPEED)
        pygame.display.flip()

    pygame.quit()
