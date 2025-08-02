import unittest

from itertools import product

import numpy.testing as npt

from tetris.core.tetrimino_factory import TetriminoFactory
from tetris.core.tetrimino_type import TetriminoType


class TestTetriminoFactory(unittest.TestCase):
    def test_same_seed(self):
        """Test tetriminos generation with same random seed."""
        seed = 1234
        n_tetrimino = 1000
        tetrimino_factory0 = TetriminoFactory(seed)
        tetriminos0 = []
        for _ in range(n_tetrimino):
            tetriminos0.append(tetrimino_factory0.generate_random())

        tetrimino_factory1 = TetriminoFactory(seed)
        tetriminos1 = []
        for _ in range(n_tetrimino):
            tetriminos1.append(tetrimino_factory1.generate_random())
        self.assertEqual(tetriminos0, tetriminos1)

    def test_different_seed(self):
        """Test tetriminos generation with different random seeds."""
        n_tetrimino = 100
        tetrimino_factory0 = TetriminoFactory(-1)
        tetriminos0 = []
        for _ in range(n_tetrimino):
            tetriminos0.append(tetrimino_factory0.generate_random())

        tetrimino_factory1 = TetriminoFactory(-9)
        tetriminos1 = []
        for _ in range(n_tetrimino):
            tetriminos1.append(tetrimino_factory1.generate_random())
        self.assertNotEqual(tetriminos0, tetriminos1)

    def test_fixed_generation(self):
        """Test deterministic tetrimino generation."""
        tetrimino_factory = TetriminoFactory()
        tetrimino_list = tetrimino_factory.tetrimino_choices
        rotation_list = tetrimino_factory.rotation_choices
        for name, rot in product(tetrimino_list, rotation_list):
            ref = TetriminoType[name].shape(rot)
            _, _, tgt = tetrimino_factory.generate_fixed(name, rot)
            npt.assert_array_equal(tgt, ref)


if __name__ == '__main__':
    unittest.main()
