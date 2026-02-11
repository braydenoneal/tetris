from dataclasses import dataclass


@dataclass
class Shape:
    color: int
    tiles: list[tuple[int, int]]


SHAPES: list[Shape] = [
    Shape(0x00FFFF, [(0, 0), (1, 0), (2, 0), (3, 0)]),  # Cyan I
    Shape(0xFFFF00, [(0, 0), (1, 0), (0, 1), (1, 1)]),  # Yellow O
    Shape(0xFF00FF, [(0, 0), (1, 0), (2, 0), (1, 1)]),  # Purple T
    Shape(0x00FF00, [(1, 0), (2, 0), (0, 1), (1, 1)]),  # Green S
    Shape(0xFF0000, [(0, 0), (1, 0), (1, 1), (2, 1)]),  # Red Z
    Shape(0x0000FF, [(0, 0), (1, 0), (2, 0), (2, 1)]),  # Blue J
    Shape(0xFF7F00, [(0, 0), (1, 0), (2, 0), (0, 1)]),  # Orange L
]


def shape_width(shape: Shape) -> int:
    return max(x for x, _ in shape.tiles) + 1
