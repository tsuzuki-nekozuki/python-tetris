import unittest

from tetris.core.tetrimino import Tetrimino
from tetris.core.tetrimino_type import TetriminoType

class TestTetrimino(unittest.TestCase):
    def test_rotate_clockwise(self):
        """Test clockwise rotation."""
        current_rot = 1
        next_rot = 0
        tetrimino = Tetrimino(TetriminoType.I, pos_x=0, pos_y=0,
                              rot=current_rot)
        tetrimino.rotate_clockwise()
        self.assertEqual(tetrimino.rot, next_rot)

    def test_rotate_counter_clockwise(self):
        """Test clockwise rotation."""
        current_rot = 0
        next_rot = 3
        tetrimino = Tetrimino(TetriminoType.T, pos_x=0, pos_y=0,
                              rot=current_rot)
        tetrimino.rotate_counter_clockwise()
        self.assertEqual(tetrimino.rot, next_rot)

    def test_move_left(self):
        """Test left move."""
        current_pos_x = 5
        next_pos_x = 4
        tetrimino = Tetrimino(TetriminoType.T, pos_x=current_pos_x, pos_y=0,
                              rot=1)
        tetrimino.move_left()
        self.assertEqual(tetrimino.pos_x, next_pos_x)

    def test_move_right(self):
        """Test right move."""
        current_pos_x = 10
        next_pos_x = 11
        tetrimino = Tetrimino(TetriminoType.T, pos_x=current_pos_x, pos_y=0,
                              rot=1)
        tetrimino.move_right()
        self.assertEqual(tetrimino.pos_x, next_pos_x)

    def test_move_down(self):
        """Test down move."""
        current_pos_y = 10
        next_pos_y = 9
        tetrimino = Tetrimino(TetriminoType.T, pos_x=5, pos_y=current_pos_y,
                              rot=2)
        tetrimino.move_down()
        self.assertEqual(tetrimino.pos_y, next_pos_y)

    def test_rotate_clockwise_raises_value_error(self):
        """Test rotation with None."""
        t = Tetrimino(TetriminoType.Z, pos_x=0, pos_y=0, rot=None)
        with self.assertRaises(ValueError) as cm:
            t.rotate_clockwise()
        self.assertIn('Rotation is not set', str(cm.exception))

    def test_rotate_counter_clockwise_raises_value_error(self):
        """Test rotation with None."""
        t = Tetrimino(TetriminoType.J)
        with self.assertRaises(ValueError) as cm:
            t.rotate_clockwise()
        self.assertIn('Rotation is not set', str(cm.exception))

    def test_move_down_raises_value_error(self):
        """Test position with None."""
        t = Tetrimino(TetriminoType.I, pos_x=0, pos_y=None, rot=0)
        with self.assertRaises(ValueError) as cm:
            t.move_down()
        self.assertIn('Vertical position is not set', str(cm.exception))

    def test_move_left_raises_value_error(self):
        """Test position with None."""
        t = Tetrimino(TetriminoType.L, pos_x=None, pos_y=0, rot=0)
        with self.assertRaises(ValueError) as cm:
            t.move_left()
        self.assertIn('Horizontal position is not set', str(cm.exception))

    def test_move_right_raises_value_error(self):
        """Test position with None."""
        t = Tetrimino(TetriminoType.O, pos_x=None, pos_y=0, rot=0)
        with self.assertRaises(ValueError) as cm:
            t.move_right()
        self.assertIn('Horizontal position is not set', str(cm.exception))


if __name__ == '__main__':
    unittest.main()
