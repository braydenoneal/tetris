import pygame
from pygame import Surface, Event

from board import Board, X_TILES, Y_TILES, BOARD_COLOR, BOARD_BORDER_COLOR
from turn import Turn

TILE_SIZE = 20
BACKGROUND_COLOR = 0x222222


class UI:
    def __init__(self, screen: Surface, board: Board, turn: Turn):
        self.screen: Surface = screen
        self.board: Board = board
        self.turn = turn
        self.first_shift_delay = 10
        self.repeat_shift_delay = 5
        self.left_counter = 0
        self.right_counter = 0

    def handle_keys(self):
        keys = pygame.key.get_pressed()

        self.turn.delay = 2 if keys[pygame.K_DOWN] else 10

        f = self.first_shift_delay
        r = self.repeat_shift_delay

        if keys[pygame.K_LEFT]:
            c = self.left_counter

            if c == 0 or (c >= f and (c - f) % r == 0):
                self.turn.piece.move_left()

                if not self.board.is_valid_piece(self.turn.piece):
                    self.turn.piece.move_right()

            self.left_counter += 1
        else:
            self.left_counter = 0

        if keys[pygame.K_RIGHT]:
            c = self.right_counter

            if c == 0 or (c >= f and (c - f) % r == 0):
                self.turn.piece.move_right()

                if not self.board.is_valid_piece(self.turn.piece):
                    self.turn.piece.move_left()

            self.right_counter += 1
        else:
            self.right_counter = 0

    def handle_input(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.turn.piece.rotate_cw()

                if not self.board.is_valid_piece(self.turn.piece):
                    self.turn.piece.rotate_ccw()
            elif event.key == pygame.K_SPACE:
                self.turn.place_now()

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self._render_board()
        self._render_ghost_piece()
        self._render_piece()
        self._render_piece_preview()
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

    def _render_tiles(self, tiles: list[tuple[int, int]], color: int):
        board_x_start, board_y_start = self._get_board_start()

        for x, y in tiles:
            x_start = board_x_start + x * TILE_SIZE
            y_start = board_y_start + y * TILE_SIZE

            pygame.draw.rect(self.screen, color, (x_start, y_start, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, BOARD_BORDER_COLOR, (x_start, y_start, TILE_SIZE, TILE_SIZE), 1)

    def _render_piece(self):
        piece = self.turn.piece
        self._render_tiles(piece.tiles(), piece.shape.color)

    def _render_ghost_piece(self):
        piece = self.turn.get_ghost()
        self._render_tiles(piece.tiles(), piece.shape.ghost_color)

    def _render_piece_preview(self):
        for index, shape in enumerate(self.turn.random.get_preview()):
            tiles = [(x - 5, y + index * 4) for x, y in shape.tiles]
            self._render_tiles(tiles, shape.color)
