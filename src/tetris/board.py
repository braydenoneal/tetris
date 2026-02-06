from shape import Shape

X_TILES = 10
Y_TILES = 20
BOARD_COLOR = (0x44, 0x44, 0x44)
BOARD_BORDER_COLOR = (0x33, 0x33, 0x33)


class Board:
    def __init__(self):
        self.grid: list[list[Shape | None]] = [[None for _ in range(Y_TILES)] for _ in range(X_TILES)]
