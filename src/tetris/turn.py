import random

from board import Board, Y_TILES
from piece import Piece
from shape import Shape, SHAPES


class Turn:
    def __init__(self, board: Board):
        self.board = board
        self.random = RandomPieceGenerator()
        self.piece = self.random.next_piece()

        while self.piece.shape.name == "S" or self.piece.shape.name == "Z":
            self.random = RandomPieceGenerator()
            self.piece = self.random.next_piece()

        self.counter = 0
        self.delay = 10
        self.stop_delay = False

    def step(self):
        self.counter += 1

        if self.counter < self.delay:
            return True

        self.counter = 0

        if self.piece_should_stop(self.piece):
            if not self.stop_delay:
                self.stop_delay = True
                return True
            else:
                self.stop_delay = False

            self.place_piece()
            self.board.step()
            self.piece = self.random.next_piece()

            if self.piece_should_stop(self.piece):
                return False

        self.piece.y += 1

        return True

    def place_now(self):
        while not self.piece_should_stop(self.piece):
            self.piece.y += 1

        self.place_piece()
        self.board.step()
        self.piece = self.random.next_piece()

    def piece_should_stop(self, piece: Piece) -> bool:
        for x, y in piece.tiles():
            if y >= Y_TILES - 1:
                return True

            if self.board.grid[x][y + 1]:
                return True

        return False

    def place_piece(self):
        for x, y in self.piece.tiles():
            self.board.grid[x][y] = self.piece.shape

    def get_ghost(self) -> Piece:
        piece = Piece(self.piece.shape)
        piece.x = self.piece.x
        piece.y = self.piece.y
        piece.rotations = self.piece.rotations

        while not self.piece_should_stop(piece):
            piece.y += 1

        return piece


class RandomPieceGenerator:
    def __init__(self):
        self.index = 0
        self.shapes = SHAPES.copy()
        self.next_shapes = SHAPES.copy()
        random.shuffle(self.shapes)
        random.shuffle(self.next_shapes)

    def next_piece(self) -> Piece:
        piece = Piece(self.shapes[self.index])
        self.index += 1

        if self.index >= len(SHAPES):
            self.index = 0
            self.shapes = self.next_shapes.copy()
            random.shuffle(self.next_shapes)

        return piece

    def get_preview(self) -> list[Shape]:
        shapes: list[Shape] = []

        for i in range(self.index, self.index + 3):
            if i < len(SHAPES):
                shapes.append(self.shapes[i])
            else:
                shapes.append(self.next_shapes[i - len(SHAPES)])

        return shapes
