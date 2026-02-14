import math

from board import Board, X_TILES
from shape import Shape, shape_width


class Piece:
    def __init__(self, shape: Shape, board: Board):
        self.shape = shape
        self.board = board
        self.x = X_TILES // 2 - math.ceil(shape_width(shape) / 2)
        self.y = 0
        self.rotations = 0  # 1-3

    def move_left(self):
        self.x -= 1

        if not self.board.is_valid_piece(self):
            self.x += 1

    def move_right(self):
        self.x += 1

        if not self.board.is_valid_piece(self):
            self.x -= 1

    def rotate_cw(self):
        if self.shape.name == "O":
            return

        self.rotations = (self.rotations + 1) % 4

        if self.board.is_valid_piece(self):
            return

        tests = [
            [(1, 0), (1, -1), (0, 2), (1, 2)],
            [(-1, 0), (-1, 1), (0, -2), (-1, -2)],
            [(-1, 0), (-1, -1), (0, 2), (-1, 2)],
            [(1, 0), (1, 1), (0, -2), (1, -2)],
        ] if self.shape.name != "I" else [
            [(-2, 0), (1, 0), (-2, 1), (1, -2)],
            [(-1, 0), (2, 0), (-1, -2), (2, 1)],
            [(2, 0), (-1, 0), (2, -1), (-1, 2)],
            [(1, 0), (-2, 0), (1, 2), (-2, -1)],
        ]

        prev_x = self.x
        prev_y = self.y

        for x, y in tests[self.rotations]:
            self.x = prev_x + x
            self.y = prev_y + y

            if self.board.is_valid_piece(self):
                return

        self.x = prev_x
        self.y = prev_y
        self.rotations = (self.rotations - 1) % 4

    def rotate_ccw(self):
        if self.shape.name == "O":
            return

        self.rotations = (self.rotations - 1) % 4

        if self.board.is_valid_piece(self):
            return

        tests = [
            [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
            [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
            [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
            [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
        ] if self.shape.name != "I" else [
            [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],
            [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],
            [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],
            [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],
        ]

        prev_x = self.x
        prev_y = self.y

        for x, y in tests[self.rotations]:
            self.x = prev_x + x
            self.y = prev_y + y

            if self.board.is_valid_piece(self):
                return

        self.x = prev_x
        self.y = prev_y
        self.rotations = (self.rotations + 1) % 4

    def tiles(self):
        tiles = self.shape.tiles
        center_x, center_y = self.shape.center

        for _ in range(self.rotations):
            tiles = [(x - center_x, y - center_y) for x, y in tiles]
            tiles = [(-y, x) for x, y in tiles]
            tiles = [(round(x + center_x), round(y + center_y)) for x, y in tiles]

        return [(x + self.x, y + self.y) for x, y, in tiles]
