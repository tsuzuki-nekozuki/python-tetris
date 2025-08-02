import unittest

import numpy as np

from tetris.core.tetrimino_type import TetriminoType


class TestTetriminoType(unittest.TestCase):
    def test_id_and_shapes_exist(self):
        """Test if Tetriminos are defined properly."""
        id_list = sorted([t.id for t in TetriminoType])
        self.assertEqual(id_list, list(range(1, len(TetriminoType) + 1)))
        for t in TetriminoType:
            self.assertIsInstance(t.id, int)
            self.assertIsInstance(t.shapes, list)
            self.assertIn(len(t.shapes), [1, 2, 4])

    def test_shape_returns_correct_rotation(self):
        """Test rotation."""
        for t in TetriminoType:
            num_rotations = len(t.shapes)
            for rot in range(-2 * num_rotations, 2 * num_rotations):
                expected = t.shapes[rot % num_rotations]
                actual = t.shape(rot)
                np.testing.assert_array_equal(actual, expected)

    def test_shape_return_type(self):
        """Test shape instance."""
        for t in TetriminoType:
            for rot in range(len(t.shapes)):
                self.assertIsInstance(t.shape(rot), np.ndarray)

    def test_shape_values_match_id(self):
        """Test if shape values and id are matching."""
        for t in TetriminoType:
            for shape in t.shapes:
                values = shape.flatten()
                nonzero = values[values > 0]
                self.assertTrue(np.all(nonzero == t.id))


if __name__ == '__main__':
    unittest.main()
