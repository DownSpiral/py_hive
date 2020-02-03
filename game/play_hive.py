from draw import Draw

GAME_SPEED = 60

if __name__ == '__main__':
    draw = Draw()

    gameExit = False
    while not gameExit:
        draw.handle_events()
        draw.update(GAME_SPEED)
