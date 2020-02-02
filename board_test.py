from board import Coord
from board import Board
import unittest

WIDTH = 10
HEIGHT = 10

class TestBoard(unittest.TestCase):
    """
    Test initializer
    """
    def __init__(self, *args, **kwargs):
        # what does this actually do?
        # without it, we cant bind attributes to self
        super(TestBoard, self).__init__(*args, **kwargs)

        self.b = Board(WIDTH, HEIGHT)

    def test_0_width_and_height(self):
        self.assertEqual(self.b.width, WIDTH)
        self.assertEqual(self.b.height, HEIGHT)

    def test_1__str__(self):
        self.assertEqual(str(self.b), '\n'.join(' '.join(map(str, sl)) for sl in self.b.board))

    def test_2_get_tile(self):
        x, y = 3, 4
        subject = self.b.getTile(x, y)
        self.assertEqual(subject.coord.x, x)
        self.assertEqual(subject.coord.y, y)

    def test_3_surrounding_tiles(self):
        x, y = 3, 3
        # This intermediate coord class is kinda annoying to work with.
        subject = [(tile.coord.x, tile.coord.y) for tile in self.b.surroundingTiles(Coord(x, y))]
        for (i, j) in [(2, 3), (4, 3), (3, 2), (3, 4)]:
            self.assertTrue((i, j) in subject)

if __name__ == '__main__':
    unittest.main()
