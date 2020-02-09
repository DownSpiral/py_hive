from random import random

def random_color():
    return (255 * random(), 255 * random(), 255 * random())

FOOD_COLORS = {
    'dense': (47, 110, 29),
    'medium': (82, 168, 56),
    'light': (126, 230, 94)
}

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'brown': (150, 75, 0),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}
