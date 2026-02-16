import random

from board import Board, Y_TILES, VISIBLE_Y_TILES
from piece import Piece
from shape import Shape, SHAPES


class Turn:
    def __init__(self, board: Board):
        self.board = board
        self.random = RandomPieceGenerator(self.board)
        self.piece = self.random.next_piece()
        self.hold_piece: Piece | None = None
        self.can_hold = True

        while self.piece.shape.name == "S" or self.piece.shape.name == "Z":
            self.random = RandomPieceGenerator(self.board)
            self.piece = self.random.next_piece()

        self.fast_delay = 2
        self.slow_delay = 10
        self.delay = self.slow_delay
        self.counter = 0

        self.lock_delay = 3
        self.lock_counter = 0

    def step(self):
        self.counter += 1

        if self.counter < self.delay:
            return True

        self.counter = 0

        if self.piece_should_stop(self.piece):
            self.lock_counter += 1

            if self.lock_counter < self.lock_delay:
                return True

            self.lock_counter = 0
            self.place_piece()
            self.board.step()
            self.piece = self.random.next_piece()

            return not self.spawns_overlapping(self.piece)

        self.lock_counter = 0
        self.piece.y += 1

        return True

    def place_now(self):
        while not self.piece_should_stop(self.piece):
            self.piece.y += 1

        self.place_piece()
        self.board.step()
        self.piece = self.random.next_piece()

    def spawns_overlapping(self, piece: Piece) -> bool:
        for x, y in piece.tiles():
            if self.board.grid[x][y]:
                return True

        return False

    def piece_should_stop(self, piece: Piece) -> bool:
        for x, y in piece.tiles():
            if y >= Y_TILES - 1 or self.board.grid[x][y + 1]:
                return True

        return False

    def place_piece(self):
        self.can_hold = True
        all_above_playfield = True

        for x, y in self.piece.tiles():
            self.board.grid[x][y] = self.piece.shape

            if y >= VISIBLE_Y_TILES:
                all_above_playfield = False

        if all_above_playfield:
            exit()

    def get_ghost(self) -> Piece:
        piece = Piece(self.piece.shape, self.board)
        piece.x = self.piece.x
        piece.y = self.piece.y
        piece.rotations = self.piece.rotations

        while not self.piece_should_stop(piece):
            piece.y += 1

        return piece

    def hold(self):
        if self.can_hold:
            self.can_hold = False
            next_piece = self.hold_piece if self.hold_piece else self.random.next_piece()
            self.hold_piece = Piece(self.piece.shape, self.board)
            self.piece = next_piece


class RandomPieceGenerator:
    def __init__(self, board: Board):
        self.board = board
        self.index = 0
        self.shapes = SHAPES.copy()
        self.next_shapes = SHAPES.copy()
        random.shuffle(self.shapes)
        random.shuffle(self.next_shapes)

    def next_piece(self) -> Piece:
        piece = Piece(self.shapes[self.index], self.board)
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
