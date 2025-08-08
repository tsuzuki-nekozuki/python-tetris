from ..core.board import Board, MoveType
from ..core.tetrimino_factory import TetriminoFactory


class TetrisCli:
    def __init__(self, lock_delay_thr: int = 4):
        self.board = Board()
        self.tetrimino_factory = TetriminoFactory()
        self.lock_delay_thr = lock_delay_thr
        self.lock_delay_counter = 0
        self.is_playing_status = True

    def create_new_tetrimino(self):
        new_tetrimino, rot = self.tetrimino_factory.generate_random()
        if not self.board.create_new_tetrimino(new_tetrimino, rot):
            self.is_playing_status = False

    def move_left(self):
        self.board.move_tetrimino(MoveType.LEFT)

    def move_right(self):
        self.board.move_tetrimino(MoveType.RIGHT)

    def move_down(self):
        status = self.board.move_tetrimino(MoveType.DOWN)
        if status:
            self.lock_delay_counter = 0
        else:
            self.lock_delay_counter += 1
        if self.lock_delay_counter < self.lock_delay_thr:
            self.step()

    def rotate_cw(self):
        self.board.move_tetrimino(MoveType.ROTATE_CW)

    def rotate_ccw(self):
        self.board.move_tetrimino(MoveType.ROTATE_CCW)

    def step(self):
        if not self.is_playing_status:
            return
        status = self.board.move_tetrimino(MoveType.DOWN)
        if status:
            self.lock_delay_counter = 0
        else:
            self.lock_delay_counter += 1
        print('count lock', self.lock_delay_counter)
        if self.lock_delay_counter >= self.lock_delay_thr:
            self.board.update_play_field()
            self.create_new_tetrimino()

    def is_game_over(self):
        return not self.is_playing_status

    def render_data(self) -> dict:
        return {
            'board': self.board.get_play_field(),
            'active': self.board.get_active_field(),
        }
