import random

from board import Board, Y_TILES
from piece import Piece
from shape import SHAPES


class Turn:
    def __init__(self, board: Board):
        self.board = board
        self.piece = Piece(random.choice(SHAPES))
        self.counter = 0
        self.delay = 30

    def step(self):
        self.counter += 1

        if self.counter >= self.delay:
            self.counter = 0
            self.piece.y += 1

            if self.piece_should_stop(self.piece):
                self.place_piece(self.piece)
                self.piece = Piece(random.choice(SHAPES))

    def piece_should_stop(self, piece: Piece) -> bool:
        for x, y in piece.tiles():
            if y == Y_TILES - 1:
                return True

            if self.board.grid[x][y + 1]:
                return True

        return False

    def place_piece(self, piece: Piece):
        for x, y in piece.tiles():
            self.board.grid[x][y] = piece.shape
