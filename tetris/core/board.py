import copy
import math

from enum import Enum

import numpy as np

from numpy.typing import NDArray

from .tetrimino import Tetrimino
from .tetrimino_type import TetriminoType


class MoveType(Enum):
    NO_MOVE = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    DROP = 4
    ROTATE_CW = 5
    ROTATE_CCW = 6


class Board:
    def __init__(self, width: int = 10, height: int = 20):
        self.width: int = width
        self.height: int = height
        self.max_tetrimino_size = max([i.size for i in TetriminoType])
        self.wall_id = len(TetriminoType) + 1
        self.ceil_margin: int = self.max_tetrimino_size - 1
        self.floor_margin: int = self.max_tetrimino_size - 1
        self.side_margin: int = math.ceil(self.max_tetrimino_size / 2)
        self.max_width = self.width + self.side_margin * 2
        self.max_height = self.height + self.ceil_margin + self.floor_margin
        self.tetris_field: NDArray[np.uint8] = self._init_field()
        self.active_tetrimino: Tetrimino | None = None

    def _init_field(self):
        w = self.width + self.side_margin * 2
        h = self.height + self.ceil_margin + self.floor_margin
        tetris_field = np.full((h, w), self.wall_id).astype(np.uint8)
        tetris_field[0:self.max_height - self.floor_margin,
                     self.side_margin:self.width + self.side_margin] = 0
        return tetris_field

    def create_new_tetrimino(self, tetrimino: TetriminoType, rot: int) -> bool:
        pos_x = math.floor((self.max_width - tetrimino.size) / 2)
        pos_y = self.max_tetrimino_size - tetrimino.size
        new_tetrimino = Tetrimino(tetrimino, pos_x, pos_y, rot)
        if self._is_overlapping(new_tetrimino):
            return False
        self.active_tetrimino = new_tetrimino
        return True

    def move_tetrimino(self, move: MoveType) -> bool:
        collision, next_tetrimino = self.will_collide(move)
        if not collision:
            self.active_tetrimino = next_tetrimino
            return True
        elif next_tetrimino is None:
            raise ValueError('Unknown MoveType detected.')
        return False

    def get_active_field(self, no_margin: bool = True) -> NDArray[np.uint8]:
        active_field = np.zeros((self.max_height, self.max_width),
                                dtype=np.uint8)
        x1 = self.active_tetrimino.pos_x
        x2 = x1 + self.active_tetrimino.size
        y1 = self.active_tetrimino.pos_y
        y2 = y1 + self.active_tetrimino.size
        active_field[y1:y2, x1:x2] = self.active_tetrimino.get_state()
        if no_margin:
            active_field = active_field[
                self.ceil_margin:self.ceil_margin + self.height,
                self.side_margin:self.side_margin + self.width
                ]
        return active_field

    def get_play_field(self, no_margin: bool = True) -> NDArray[np.uint8]:
        current_field = self.tetris_field.copy()
        if no_margin:
            current_field = current_field[
                self.ceil_margin:self.ceil_margin + self.height,
                self.side_margin:self.side_margin + self.width
                ]
        return current_field

    def update_play_field(self) -> int:
        self.tetris_field += self.get_active_field(no_margin=False)
        self.active_tetrimino = None
        filled_lines = np.where(~np.any(
            self.tetris_field[:self.max_height - self.floor_margin] == 0,
            axis=1))
        filled_lines = filled_lines[0].tolist()
        self.delete_lines(filled_lines)
        return len(filled_lines)

    def delete_lines(self, cleared_lines: list[int]):
        f_line_deleted = np.delete(self.tetris_field, cleared_lines, axis=0)
        f_new_add_lines = np.full((len(cleared_lines), self.max_width),
                                  self.wall_id).astype(np.uint8)
        f_new_add_lines[:, self.side_margin:self.width + self.side_margin] = 0
        self.tetris_field = np.vstack([f_new_add_lines, f_line_deleted])

    def will_collide(self, move: MoveType) -> tuple[bool, Tetrimino | None]:
        if move == MoveType.LEFT:
            has_collision, next_tetrimino = self._will_collide_left()
        elif move == MoveType.RIGHT:
            has_collision, next_tetrimino = self._will_collide_right()
        elif move == MoveType.DOWN:
            has_collision, next_tetrimino = self._will_collide_down()
        elif move == MoveType.ROTATE_CW:
            has_collision, next_tetrimino = self._will_not_rotate_cw()
        elif move == MoveType.ROTATE_CCW:
            has_collision, next_tetrimino = self._will_not_rotate_ccw()
        else:
            has_collision = True
            next_tetrimino = None
        return has_collision, next_tetrimino

    def _will_collide_left(self) -> tuple[bool, Tetrimino]:
        ghost_tetrimino = copy.copy(self.active_tetrimino)
        ghost_tetrimino.move_left()
        return self._is_overlapping(ghost_tetrimino), ghost_tetrimino

    def _will_collide_right(self) -> tuple[bool, Tetrimino]:
        ghost_tetrimino = copy.copy(self.active_tetrimino)
        ghost_tetrimino.move_right()
        return self._is_overlapping(ghost_tetrimino), ghost_tetrimino

    def _will_collide_down(self) -> tuple[bool, Tetrimino]:
        ghost_tetrimino = copy.copy(self.active_tetrimino)
        ghost_tetrimino.move_down()
        return self._is_overlapping(ghost_tetrimino), ghost_tetrimino

    def _will_not_rotate_cw(self) -> tuple[bool, Tetrimino]:
        ghost_tetrimino = copy.copy(self.active_tetrimino)
        ghost_tetrimino.rotate_clockwise()
        return self._is_overlapping(ghost_tetrimino), ghost_tetrimino

    def _will_not_rotate_ccw(self) -> tuple[bool, Tetrimino]:
        ghost_tetrimino = copy.copy(self.active_tetrimino)
        ghost_tetrimino.rotate_counter_clockwise()
        return self._is_overlapping(ghost_tetrimino), ghost_tetrimino

    def _is_overlapping(self, tetrimino: Tetrimino) -> bool:
        x1 = tetrimino.pos_x
        x2 = x1 + tetrimino.size
        y1 = tetrimino.pos_y
        y2 = y1 + tetrimino.size
        cropped = self.tetris_field[y1:y2, x1:x2]
        return np.any(np.logical_and(tetrimino.get_state() > 0, cropped > 0))
