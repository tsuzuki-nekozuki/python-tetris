import unittest

from tetris.core.board import Board, MoveType
from tetris.core.tetrimino import Tetrimino
from tetris.core.tetrimino_factory import TetriminoFactory
from tetris.core.tetrimino_type import TetriminoType


class TestBoard(unittest.TestCase):
    def test_lock_and_delete_line(self):
        board = Board()

        x1 = board.side_margin + 1
        x2 = board.side_margin + board.width
        y1 = board.ceil_margin + board.height - 4
        y2 = board.ceil_margin + board.height
        board.tetris_field[y1:y2, x1:x2] = 3

        tetrimino = Tetrimino(TetriminoType.I,
                              pos_x=0,
                              pos_y=board.ceil_margin + board.height - 4,
                              rot=1)
        board.active_tetrimino = tetrimino
        board.update_play_field()

        x1 = board.side_margin 
        x2 = board.side_margin + board.width
        y1 = 0
        y2 = board.max_height - board.floor_margin
        self.assertTrue((board.tetris_field[y1:y2, x2:x1] == 0).all())

    def test_not_create_new_tetrimino(self):
        board = Board()
        tetrimino_factory = TetriminoFactory()

        x1 = board.side_margin
        x2 = board.side_margin + board.width
        y1 = board.ceil_margin
        y2 = board.ceil_margin + board.height
        board.tetris_field[y1:y2, x1:x2] = 7

        tetrimino, rot = tetrimino_factory.generate_fixed('T', 1)
        self.assertFalse(board.create_new_tetrimino(tetrimino, rot))

    def test_create_new_tetrimino(self):
        board = Board()
        tetrimino_factory = TetriminoFactory()

        x1 = board.side_margin
        x2 = board.side_margin + board.width
        y1 = board.ceil_margin + 1
        y2 = board.ceil_margin + board.height
        board.tetris_field[y1:y2, x1:x2] = 7

        tetrimino, rot = tetrimino_factory.generate_fixed('O', 0)
        self.assertTrue(board.create_new_tetrimino(tetrimino, rot))

    def test_move_and_lock(self):
        board = Board()
        tetrimino_factory = TetriminoFactory()

        x1 = board.side_margin
        x2 = board.side_margin + board.width
        y1 = board.ceil_margin + 1
        y2 = board.ceil_margin + board.height
        board.tetris_field[y1:y2, x1:x2] = 7

        tetrimino, rot = tetrimino_factory.generate_fixed('L', 0)
        board.create_new_tetrimino(tetrimino, rot)

        # pos_x: 8 -> 7
        board.active_tetrimino.move_left()
        
        self.assertEqual(board.active_tetrimino.pos_x, 7)

