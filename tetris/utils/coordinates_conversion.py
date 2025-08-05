def to_numpy_index(pos_x: int, pos_y: int) -> tuple[int, int]:
    """
    Convert game coordinates (x, y) to numpy array index (row, col).

    Args:
        pos_x (int): Horizontal position in game coordinates.
        pos_y (int): Vertical position in game coordinates.

    Returns:
        tuple[int, int]: (row, col) for numpy indexing.
    """
    return pos_y, pos_x


def to_cv_point(pos_x: int, pos_y: int) -> tuple[int, int]:
    """
    Convert game coordinates (x, y) to OpenCV drawing point (x, y).
    OpenCV functions like cv2.rectangle expect (x, y).

    Args:
        pos_x (int): Horizontal position in game coordinates.
        pos_y (int): Vertical position in game coordinates.

    Returns:
        tuple[int, int]: (x, y) for OpenCV drawing.
    """
    return pos_x, pos_y


def numpy_index_to_game(row: int, col: int) -> tuple[int, int]:
    """
    Convert numpy array index (row, col) to game coordinates (x, y).
    Args:
        row (int): Horizontal position in numpy indexing.
        col (int): Vertical position in numpy indexing.

    Returns:
        tuple[int, int]: (x, y) for OpenCV drawing.
    """
    return col, row
