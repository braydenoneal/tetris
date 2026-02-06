from piece import Piece
from shape import Shape

X_TILES = 10
Y_TILES = 20
BOARD_COLOR = (0x44, 0x44, 0x44)
BOARD_BORDER_COLOR = (0x33, 0x33, 0x33)


class Board:
    def __init__(self):
        self.grid: list[list[Shape | None]] = [[None for _ in range(Y_TILES)] for _ in range(X_TILES)]

    def is_valid_piece(self, piece: Piece) -> bool:
        for x, y in piece.tiles():
            if x < 0 or y < 0 or x >= X_TILES or y >= Y_TILES or self.grid[x][y]:
                return False

        return True

    def _move_rows(self, y: int):
        for y in range(y, -1, -1):
            for x in range(X_TILES):
                if y == 0:
                    self.grid[x][y] = None
                else:
                    self.grid[x][y] = self.grid[x][y - 1]

    def step(self):
        for y in range(Y_TILES - 1, -1, -1):
            row_has_empty = False

            for x in range(X_TILES):
                if not self.grid[x][y]:
                    row_has_empty = True
                    break

            if not row_has_empty:
                self._move_rows(y)
                self.step()
                break
