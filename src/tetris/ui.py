import pygame
from pygame import Surface, Event

from board import Board, X_TILES, Y_TILES, BOARD_COLOR, BOARD_BORDER_COLOR
from turn import Turn

TILE_SIZE = 20
BACKGROUND_COLOR = (0x22, 0x22, 0x22)


class UI:
    def __init__(self, screen: Surface, board: Board, turn: Turn):
        self.screen: Surface = screen
        self.board: Board = board
        self.turn = turn

    def handle_input(self, event: Event):
        keys = pygame.key.get_pressed()

        self.turn.delay = 2 if keys[pygame.K_DOWN] else 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.turn.piece.move_left()

                if not self.board.is_valid_piece(self.turn.piece):
                    self.turn.piece.move_right()
            elif event.key == pygame.K_RIGHT:
                self.turn.piece.move_right()

                if not self.board.is_valid_piece(self.turn.piece):
                    self.turn.piece.move_left()
            elif event.key == pygame.K_UP:
                self.turn.piece.rotate_cw()

                if not self.board.is_valid_piece(self.turn.piece):
                    self.turn.piece.rotate_ccw()

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self._render_board()
        self._render_piece()
        pygame.display.flip()

    def _get_board_start(self) -> tuple[int, int]:
        screen_x_center = self.screen.get_width() // 2
        screen_y_center = self.screen.get_height() // 2

        board_x_center = X_TILES * TILE_SIZE // 2
        board_y_center = Y_TILES * TILE_SIZE // 2

        board_x_start = screen_x_center - board_x_center
        board_y_start = screen_y_center - board_y_center

        return board_x_start, board_y_start

    def _render_board(self):
        board_x_start, board_y_start = self._get_board_start()

        for x in range(X_TILES):
            for y in range(Y_TILES):
                x_start = board_x_start + x * TILE_SIZE
                y_start = board_y_start + y * TILE_SIZE

                shape = self.board.grid[x][y]

                pygame.draw.rect(self.screen, shape.color if shape else BOARD_COLOR, (x_start, y_start, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BOARD_BORDER_COLOR, (x_start, y_start, TILE_SIZE, TILE_SIZE), 1)

    def _render_piece(self):
        board_x_start, board_y_start = self._get_board_start()

        for x, y in self.turn.piece.tiles():
            x_start = board_x_start + x * TILE_SIZE
            y_start = board_y_start + y * TILE_SIZE

            pygame.draw.rect(self.screen, self.turn.piece.shape.color, (x_start, y_start, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, BOARD_BORDER_COLOR, (x_start, y_start, TILE_SIZE, TILE_SIZE), 1)
