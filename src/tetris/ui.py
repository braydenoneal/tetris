import pygame
from pygame import Surface, Event

from board import Board, COLS, ROWS, BOARD_COLOR, BOARD_BORDER_COLOR

TILE_SIZE = 20
BACKGROUND_COLOR = (0x22, 0x22, 0x22)


class UI:
    def __init__(self, screen: Surface, board: Board):
        self.screen: Surface = screen
        self.board: Board = board

    def handle_input(self, event: Event):
        pass

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self._render_board()
        pygame.display.flip()

    def _render_board(self):
        screen_x_center = self.screen.get_width() // 2
        screen_y_center = self.screen.get_height() // 2

        board_x_center = COLS * TILE_SIZE // 2
        board_y_center = ROWS * TILE_SIZE // 2

        board_x_start = screen_x_center - board_x_center
        board_y_start = screen_y_center - board_y_center

        for x in range(COLS):
            for y in range(ROWS):
                x_start = board_x_start + x * TILE_SIZE
                y_start = board_y_start + y * TILE_SIZE

                piece = self.board.grid[x][y]

                pygame.draw.rect(self.screen, piece.color if piece else BOARD_COLOR, (x_start, y_start, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BOARD_BORDER_COLOR, (x_start, y_start, TILE_SIZE, TILE_SIZE), 1)
