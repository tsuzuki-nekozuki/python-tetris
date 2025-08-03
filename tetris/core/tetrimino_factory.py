import random
import time

import numpy as np

from numpy.typing import NDArray

from .tetrimino_type import TetriminoType


class TetriminoFactory:
    def __init__(self, seed: int = -1):
        if not isinstance(seed, int) or seed < 0:
            seed = time.time_ns()
        random.seed(seed)
        self.tetrimino_choices = [i.name for i in TetriminoType]
        self.rotation_choices = [i for i in range(4)]

    def generate_random(self) -> tuple[str, int, NDArray[np.uint8]]:
        tetrimino_name = random.choice(self.tetrimino_choices)
        rotation = random.choice(self.rotation_choices)
        tetrimino = self._generate_tetrimino(tetrimino_name, rotation)
        return tetrimino_name, rotation, tetrimino

    def generate_fixed(self,
                       tetrimino_name: str,
                       rotation: int) -> tuple[str, int, NDArray[np.uint8]]:
        tetrimino = self._generate_tetrimino(tetrimino_name, rotation)
        return tetrimino_name, rotation, tetrimino

    def _generate_tetrimino(self, tetrimino_type: str, rotation: int):
        try:
            tetrimino = TetriminoType[tetrimino_type]
        except KeyError as exc:
            raise KeyError(
                    f'"{tetrimino_type}" is not a valid tetrimino type.'
                ) from exc
        return tetrimino.shape(rotation)
