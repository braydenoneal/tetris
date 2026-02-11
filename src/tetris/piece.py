import math

import board
from shape import Shape, shape_width


class Piece:
    def __init__(self, shape: Shape):
        self.shape = shape
        self.x = board.X_TILES // 2 - math.ceil(shape_width(shape) / 2)
        self.y = 0
        self.rotations = 0  # 1-3

    def _local_tiles(self):
        tiles = self.shape.tiles

        for _ in range(self.rotations):
            tiles = [(-y, x) for x, y in tiles]

        min_x = min(x for x, _ in tiles)
        min_y = min(y for _, y in tiles)

        return [(x - min_x, y - min_y) for x, y in tiles]

    def _center(self):
        tiles = self._local_tiles()

        max_x = max(x for x, _ in tiles) + 1
        max_y = max(y for _, y in tiles) + 1

        return max_x // 2, max_y // 2

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate_cw(self):
        prev_center_x, prev_center_y = self._center()

        self.rotations = (self.rotations + 1) % 4
        center_x, center_y = self._center()

        self.x += prev_center_x - center_x
        self.y += prev_center_y - center_y

    def rotate_ccw(self):
        self.rotations = (self.rotations - 1) % 4

    def tiles(self):
        return [(x + self.x, y + self.y) for x, y, in self._local_tiles()]
