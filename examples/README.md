# Examples

This directory contains sample code demonstrating how to use the `tetris` library.

## tetris_cli.py

A simple command-line Tetris game that runs in the terminal.  
The core game logic is implemented in `tetris.core`, while this CLI is intended for testing and demonstration purposes.

### How to Run

Run the following command from the project root directory:

```bash
python -m tetris.examples.tetris_cli
```

### Controls

| Key | Action                  |
| --- | ----------------------- |
| a   | Move left               |
| d   | Move right              |
| s   | Move down               |
| q   | Rotate counterclockwise |
| e   | Rotate clockwise        |
| q   | Quit game               |

### Notes

- This CLI is designed for learning, debugging, and testing the game logic.
- It can also be used for reinforcement learning experiments or automated play testing.
- No advanced UI features are implemented — it runs purely in the terminal.