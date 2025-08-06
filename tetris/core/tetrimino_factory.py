import random
import time

from .tetrimino_type import TetriminoType


class TetriminoFactory:
    def __init__(self, seed: int = -1):
        if not isinstance(seed, int) or seed < 0:
            seed = time.time_ns()
        random.seed(seed)
        self.tetrimino_choices = [i.name for i in TetriminoType]
        self.rotation_choices = [i for i in range(4)]

    def generate_random(self) -> tuple[TetriminoType, int]:
        tetrimino_name = random.choice(self.tetrimino_choices)
        rotation = random.choice(self.rotation_choices)
        tetrimino = self._generate_tetrimino(tetrimino_name)
        return tetrimino, rotation

    def generate_fixed(self, tetrimino_name: str,
                       rotation: int) -> tuple[TetriminoType, int]:
        tetrimino = self._generate_tetrimino(tetrimino_name)
        return tetrimino, rotation

    def _generate_tetrimino(self, tetrimino_name: str) -> TetriminoType:
        try:
            tetrimino = TetriminoType[tetrimino_name]
        except KeyError as exc:
            raise KeyError('"{}" is not a valid tetrimino type.'
                           .format(tetrimino_name)) from exc
        return tetrimino
