from dataclasses import dataclass


@dataclass
class Shape:
    name: str
    color: int
    ghost_color: int
    tiles: list[tuple[int, int]]


SHAPES: list[Shape] = [
    Shape("I", 0x00FFFF, 0x007F7F, [(0, 0), (1, 0), (2, 0), (3, 0)]),  # Cyan
    Shape("O", 0xFFFF00, 0x7F7F00, [(0, 0), (1, 0), (0, 1), (1, 1)]),  # Yellow
    Shape("T", 0xFF00FF, 0x7F007F, [(0, 0), (1, 0), (2, 0), (1, 1)]),  # Purple
    Shape("S", 0x00FF00, 0x007F00, [(1, 0), (2, 0), (0, 1), (1, 1)]),  # Green
    Shape("Z", 0xFF0000, 0x7F0000, [(0, 0), (1, 0), (1, 1), (2, 1)]),  # Red
    Shape("J", 0x0000FF, 0x00007F, [(0, 0), (1, 0), (2, 0), (2, 1)]),  # Blue
    Shape("L", 0xFF7F00, 0x7F4F00, [(0, 0), (1, 0), (2, 0), (0, 1)]),  # Orange
]


def shape_width(shape: Shape) -> int:
    return max(x for x, _ in shape.tiles) + 1
