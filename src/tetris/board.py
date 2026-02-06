from piece import Piece

COLS = 10
ROWS = 20
BOARD_COLOR = (0x44, 0x44, 0x44)
BOARD_BORDER_COLOR = (0x33, 0x33, 0x33)


class Board:
    def __init__(self):
        self.grid: list[list[Piece | None]] = [[None for _ in range(ROWS)] for _ in range(COLS)]
