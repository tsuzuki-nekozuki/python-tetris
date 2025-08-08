from .tetrimino_type import TetriminoType


class Tetrimino:
    def __init__(self,
                 tetrimino_type: TetriminoType,
                 pos_x: int | None = None,
                 pos_y: int | None = None,
                 rot: int | None = None):
        self.type = tetrimino_type
        # Position is top left corner of the Tetrimino
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rot = rot
        self.size = tetrimino_type.size

    def rotate_clockwise(self):
        if self.rot is None:
            raise ValueError('Rotation is not set.')
        self.rot = (self.rot + 1) % len(self.type.shapes)

    def rotate_counter_clockwise(self):
        if self.rot is None:
            raise ValueError('Rotation is not set.')
        self.rot = (self.rot - 1) % len(self.type.shapes)

    def move_down(self):
        if self.pos_y is None:
            raise ValueError('Vertical position is not set.')
        self.pos_y = self.pos_y + 1

    def move_left(self):
        if self.pos_x is None:
            raise ValueError('Horizontal position is not set.')
        self.pos_x = self.pos_x - 1

    def move_right(self):
        if self.pos_x is None:
            raise ValueError('Horizontal position is not set.')
        self.pos_x = self.pos_x + 1

    def set_state(self, rot: int, pos_x: int, pos_y: int):
        self.rot = rot % len(self.type.shapes)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_state(self):
        return self.type.shape(self.rot)