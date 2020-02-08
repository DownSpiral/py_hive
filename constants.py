from random import random

def random_color():
    return (255 * random(), 255 * random(), 255 * random())

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'brown': (150, 75, 0),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}
