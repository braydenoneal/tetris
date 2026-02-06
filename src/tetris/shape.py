from dataclasses import dataclass


@dataclass
class Shape:
    color: tuple[int, int, int]
    tiles: list[tuple[int, int]]


SHAPES: list[Shape] = [
    Shape((0x00, 0xFF, 0xFF), [(0, 0), (1, 0), (2, 0), (3, 0)]),
    Shape((0xFF, 0xFF, 0x00), [(0, 0), (1, 0), (0, 1), (1, 1)]),
    Shape((0xFF, 0x00, 0xFF), [(0, 0), (1, 0), (2, 0), (1, 1)]),
    Shape((0x00, 0x00, 0xFF), [(1, 0), (1, 1), (0, 2), (1, 2)]),
    Shape((0xFF, 0x7F, 0x00), [(0, 0), (0, 1), (0, 2), (1, 2)]),
    Shape((0x00, 0xFF, 0x00), [(1, 0), (2, 0), (0, 1), (1, 1)]),
    Shape((0xFF, 0x00, 0x00), [(0, 0), (1, 0), (1, 1), (2, 1)]),
]
