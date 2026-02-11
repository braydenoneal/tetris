import random

from board import Board, Y_TILES
from piece import Piece
from shape import SHAPES


class Turn:
    def __init__(self, board: Board):
        self.board = board
        self.piece = Piece(random.choice(SHAPES))
        self.counter = 0
        self.delay = 10
        self.stop_delay = False

    def step(self):
        self.counter += 1

        if self.counter < self.delay:
            return True

        self.counter = 0

        if self.piece_should_stop():
            if not self.stop_delay:
                self.stop_delay = True
                return True
            else:
                self.stop_delay = False

            self.place_piece(self.piece)
            self.board.step()
            self.piece = Piece(random.choice(SHAPES))

            if self.piece_should_stop():
                return False

        self.piece.y += 1

        return True

    def place_now(self):
        while not self.piece_should_stop():
            self.piece.y += 1

        self.place_piece(self.piece)
        self.board.step()
        self.piece = Piece(random.choice(SHAPES))

    def piece_should_stop(self) -> bool:
        for x, y in self.piece.tiles():
            if y >= Y_TILES - 1:
                return True

            if self.board.grid[x][y + 1]:
                return True

        return False

    def place_piece(self, piece: Piece):
        for x, y in piece.tiles():
            self.board.grid[x][y] = piece.shape
