# Tetris in Python

## Introduction

This repository is an implementation of Tetris in Python.

Key features:

- **Python-based Tetris**: Implemented entirely in Python
- **OpenCV for rendering**: The game window and graphics are drawn using OpenCV
- **Modular architecture**: Game logic (core) and UI (rendering) are separated for clarity
- **Unit testing**: Includes tests for core components such as `Tetrimino` and `Board`
- **Object-oriented design**: Class diagrams are provided below

This project focuses on learning software development practices, including:

- Requirement definition and internal design
- Class diagram and modular architecture
- Step-by-step implementation with unit tests

---

## Repository Overview

- `core/` – Core game logic (board, tetrimino, history)
- `ui/` – Rendering and window management using OpenCV
- `tests/` – Unit tests for core modules

---

## Class diagram
The following class diagram provides an overview of the core structure of this Tetris implementation, including the main classes and their relationships. It distinguishes between the game logic and the UI layer, which are designed to be modular and loosely coupled. (This diagram was generated using PlantUML.)

```plantuml
@startuml
class SceneManager {
    - scenes: Dict
    - current_scene: BaseScene
    ---
    + change_scene(scene: BaseScene)
    + update()
    + render()
    + handle_input(key: str)
    - _create_game_scene()
    - _create_menu_scene()
    - _create_pause_scene()
    - _create_game_over_scene()
    - _create_replay_scene()
}

abstract class BaseScene {
    - frame_id: int
    ---
    + update()
    + render()
    + handle_input(key: str)
}

class GameScene extends BaseScene {
    - board: Board
    - current_tetrimino: Tetrimino
    - next_tetrimino: Tetrimino
    - is_save_history: bool
    ---
    + generate_next_tetrimino()
    + save_history()
    - _count_frame()
}

class ReplayScene extends BaseScene {
    - state: str
    - speed: int
    ---
    + load_history(fname: str | Path)
    + play()
    + stop()
}

class MenuScene extends BaseScene {
    - options: dict
    - selected_option: str
}

class PauseScene extends BaseScene {
    - state: str
    ---
    + resume_game()
    + back_to_menu()
}
class GameOverScene extends BaseScene {
    - state: str
    ---
    + start_new_game()
    + back_to_menu()
}

class WindowManager {
    - title: str
    - width: int
    - height: int
    - frame: NDArray[np.uint8]
    - key: str
    ---
    + clear()
    + get_frame()
    + get_key()
    + show(frame: NDArray[np.uint8])
    + should_close()
    + close()
}

class Renderer {
    + render(SceneRenderer)
}

abstract class SceneRenderer {
    + render()
}


class GameSceneRenderer extends SceneRenderer {
    - current_board: NDArray[np.uint32]
    - next_tetrimino: TetriminoType
    - score: int
    - level: int
}

class ReplaySceneRenderer extends SceneRenderer {
    - current_board: NDArray[np.uint32]
    - next_tetrimino: TetriminoType
    - score: int
    - level: int
}

class MenuSceneRenderer extends SceneRenderer {
    - options: Dict
    - selected_option: int
}

class PauseSceneRenderer extends SceneRenderer {
    - message: str
}

class GameOverSceneRenderer extends SceneRenderer {
    - message: str
}

class TetrisCanvas {
    - board_file: Union[str, Path]
    - board_template: Dict
    - board: NDArray[np.uint8]
    - board_position: Tuple[int, int, int, int]
    - score_position: Tuple[int, int, int, int]
    - level_position: Tuple[int, int, int, int]
    - next_tetrimino_position: Tuple[int, int, int, int]
    ---
    - _set_position()
    + draw_canvas()
}

class TetriminoSkin {
    - pattern_file: str | Path
    - patterns: Dict
    - colors: Dict
    ---
    + load_skin()
}

class PlayerStatus <<dataclass>> {
    - score: int
    - lines: int
    - level: int
    ---
    + add_score(cleared_lines: int, n_fast_drop: int)
    + calculate_level(cleared_lines: int)
}

class Board {
    - play_width: int
    - play_height: int
    - side_margin: int
    - top_margin: int
    - bottom_margin: int
    - max_tetrimino_size: int
    - max_width: int
    - max_height: int
    - tetris_field: NDArray[np.uint8]
    - active_tetrimino: Tetrimino | None
    ---
    + create_new_tetrimino()
    + move_tetrimino(move: MoveType)
    + will_collide()
    + is_locked()
    + count_fast_drop()
    + reset_fast_drop()
    + update_play_field()
    + delete_lines()
    - _is_overlapping()
    - _will_collide_left()
    - _will_collide_right()
    - _will_collide_bottom()
    - _will_not_have_clockwise_rotation()
    - _will_not_have_counter_clockwise_rotation()
    - _will_collide_tetrimino()
}

Enum MoveType {
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    DROP = 4
    ROTATE_CW = 5
    ROTATE_CCW = 6
}

class Tetrimino {
    - type: TetriminoType
    - pos_x: int | None
    - pos_y: int | None
    - rot: int | None
    ---
    + rotate_clockwise()
    + rotate_counter_clockwise()
    + move_left()
    + move_right()
    + move_down()
    + set_state(rot: int, pos_x: int, pos_y: int)
}

Enum TetriminoType {
    I
    O
    T
    S
    Z
    J
    L
    ---
    - id: int
    - shapes: list[NDArray[np.uint8]]
    ---
    + shape(rotation: int)
    + rot(shape: NDArray[np.uint8])
    + size()
}

class TetriminoFactory {
    tetrimino_choices: Dict
    rotation_choices: Dict
    ---
    + generate_random()
    + generate_fixed(tetrimino_type: str, rotation: int)
    - _generate(tetrimino_type: str, rotation: int)
}

class History {
    - frame_id: int
    - input_key: str | None
    - frames: list[Frame_data]
    ---
    + save_frame(frame_id: int, frame: FrameData, input_key: str, board: list[list[int]])
    + write(fname: str | Path)
    + read(fname: str | Path)
    + get_frame(frame_id: int)
    + get_next_frame()
    + get_previous_frame()
}

class FrameData <<frozen dataclass>> {
    - tetrimino: str
    - rotation: int
    - position: set[int, int]
}

WindowManager --> SceneManager: gets key
SceneManager --> BaseScene: manages
GameScene --> Board
GameScene --> PlayerStatus
GameScene --> TetriminoFactory
ReplayScene --> Board
ReplayScene --> PlayerStatus
ReplayScene --> TetriminoFactory
ReplayScene --> History
TetriminoFactory --> TetriminoType
Tetrimino -- TetriminoType
WindowManager --> Renderer: draws
Board --> History
Board --> Tetrimino
Board -- MoveType
History --> FrameData
Renderer --> SceneRenderer: manages
GameSceneRenderer --> TetrisCanvas
GameSceneRenderer --> TetriminoSkin
@enduml
```