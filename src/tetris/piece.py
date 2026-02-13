import math

import board
from shape import Shape, shape_width


class Piece:
    def __init__(self, shape: Shape):
        self.shape = shape
        self.x = board.X_TILES // 2 - math.ceil(shape_width(shape) / 2)
        self.y = 0
        self.rotations = 0  # 1-3

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate_cw(self):
        self.rotations = (self.rotations + 1) % 4

    def rotate_ccw(self):
        self.rotations = (self.rotations - 1) % 4

    def tiles(self):
        tiles = self.shape.tiles
        center_x, center_y = self.shape.center

        for _ in range(self.rotations):
            tiles = [(x - center_x, y - center_y) for x, y in tiles]
            tiles = [(-y, x) for x, y in tiles]
            tiles = [(round(x + center_x), round(y + center_y)) for x, y in tiles]

        return [(x + self.x, y + self.y) for x, y, in tiles]
