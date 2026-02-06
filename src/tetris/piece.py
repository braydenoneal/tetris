from dataclasses import dataclass


@dataclass
class Piece:
    color: tuple[int, int, int]
    shape: list[tuple[int, int]]


PIECES: list[Piece] = [
    Piece((0x00, 0xFF, 0xFF), [(0, 0), (1, 0), (2, 0), (3, 0)]),
    Piece((0xFF, 0xFF, 0x00), [(0, 0), (1, 0), (0, 1), (1, 1)]),
    Piece((0xFF, 0x00, 0xFF), [(0, 0), (1, 0), (2, 0), (1, 1)]),
    Piece((0x00, 0x00, 0xFF), [(1, 0), (1, 1), (0, 2), (1, 2)]),
    Piece((0xFF, 0x7F, 0x00), [(0, 0), (0, 1), (0, 2), (1, 2)]),
    Piece((0x00, 0xFF, 0x00), [(1, 0), (2, 0), (0, 1), (1, 1)]),
    Piece((0xFF, 0x00, 0x00), [(0, 0), (1, 0), (1, 1), (2, 1)]),
]
