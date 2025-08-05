from enum import Enum, unique
from typing import List

import numpy as np

from numpy.typing import NDArray


@unique
class TetriminoType(Enum):
    I = (1, [np.array([[0, 0, 0, 0],
                       [1, 1, 1, 1],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]),
             np.array([[0, 0, 1, 0],
                       [0, 0, 1, 0],
                       [0, 0, 1, 0],
                       [0, 0, 1, 0]])])
    O = (2, [np.array([[2, 2],
                       [2, 2]])])
    T = (3, [np.array([[0, 3, 0],
                       [3, 3, 3],
                       [0, 0, 0]]),
             np.array([[0, 3, 0],
                       [0, 3, 3],
                       [0, 3, 0]]),
             np.array([[0, 0, 0],
                       [3, 3, 3],
                       [0, 3, 0]]),
             np.array([[0, 3, 0],
                       [3, 3, 0],
                       [0, 3, 0]])])
    S = (4, [np.array([[0, 4, 4],
                       [4, 4, 0],
                       [0, 0, 0]]),
             np.array([[0, 4, 0],
                       [0, 4, 4],
                       [0, 0, 4]])])
    Z = (5, [np.array([[5, 5, 0],
                       [0, 5, 5],
                       [0, 0, 0]]),
             np.array([[0, 5, 0],
                       [5, 5, 0],
                       [5, 0, 0]])])
    J = (6, [np.array([[0, 6, 0],
                       [0, 6, 0],
                       [6, 6, 0]]),
             np.array([[6, 0, 0],
                       [6, 6, 6],
                       [0, 0, 0]]),
             np.array([[0, 6, 6],
                       [0, 6, 0],
                       [0, 6, 0]]),
             np.array([[0, 0, 0],
                       [6, 6, 6],
                       [0, 0, 6]])])
    L = (7, [np.array([[0, 7, 0],
                       [0, 7, 0],
                       [0, 7, 7]]),
             np.array([[0, 0, 0],
                       [7, 7, 7],
                       [7, 0, 0]]),
             np.array([[7, 7, 0],
                       [0, 7, 0],
                       [0, 7, 0]]),
             np.array([[0, 0, 7],
                       [7, 7, 7],
                       [0, 0, 0]])])

    def __init__(self, id_value, shapes):
        self.id: int = id_value
        self.shapes: List[NDArray[np.uint8]] = shapes
        self.size: int = self.shapes[0].shape[0]

    def shape(self, rotation: int = 0) -> NDArray[np.uint8]:
        return self.shapes[rotation % len(self.shapes)]

    def rot(self, shape: NDArray) -> int:
        for i, ishape in enumerate(self.shapes):
            if np.array_equal(ishape, shape):
                return i
        raise ValueError('Can not find the shape.')
