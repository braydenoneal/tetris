from board import X_TILES
from shape import Shape


class Piece:
    def __init__(self, shape: Shape):
        self.shape = shape
        self.x = X_TILES // 2
        self.y = 0
        self.rotation = 0  # 1-3

    def tiles(self):
        return [(x + self.x, y + self.y) for x, y, in self.shape.tiles]
