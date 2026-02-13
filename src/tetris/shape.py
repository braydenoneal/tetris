from dataclasses import dataclass


@dataclass
class Shape:
    name: str
    color: int
    tiles: list[tuple[int, int]]
    center: tuple[float, float]


SHAPES: list[Shape] = [
    Shape("I", 0x00FFFF, [(0, 0), (1, 0), (2, 0), (3, 0)], (1.5, 0.5)),  # Cyan
    Shape("O", 0xFFFF00, [(0, 0), (1, 0), (0, 1), (1, 1)], (0.5, 0.5)),  # Yellow
    Shape("T", 0xFF00FF, [(0, 0), (1, 0), (2, 0), (1, 1)], (1, 0)),  # Purple
    Shape("S", 0x00FF00, [(1, 0), (2, 0), (0, 1), (1, 1)], (1, 0)),  # Green
    Shape("Z", 0xFF0000, [(0, 0), (1, 0), (1, 1), (2, 1)], (1, 0)),  # Red
    Shape("J", 0x0000FF, [(0, 0), (1, 0), (2, 0), (2, 1)], (1, 0)),  # Blue
    Shape("L", 0xFF7F00, [(0, 0), (1, 0), (2, 0), (0, 1)], (1, 0)),  # Orange
]


def shape_width(shape: Shape) -> int:
    return max(x for x, _ in shape.tiles) + 1
