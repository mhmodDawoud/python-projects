# Intelligent Tic-Tac-Toe

A command-line Tic-Tac-Toe game written in Python. You play as **X** against an AI that plays as **O**. The AI explores possible game states with **Breadth-First Search (BFS)** and uses **Minimax** to choose an optimal move.

## Features

- Explores possible moves with BFS.
- Evaluates wins, losses, and draws with Minimax.
- Stores each unique board-and-turn state once to avoid repeated work.
- Validates user input and prevents moves in occupied cells.
- Displays cell numbers on the board to make moves easy to enter.
- Uses only the Python standard library; no extra packages are required.

## Requirements

- Python 3

## Run the Game

Open a terminal in the folder containing `tic_tac_toe.py` and run:

```bash
python tic_tac_toe.py
```

If your system uses `python3` as the Python command, run:

```bash
python3 tic_tac_toe.py
```

## How to Play

You are **X**, and the AI is **O**. Enter the number of an empty cell when prompted. The board positions are numbered from `0` to `8`:

```text
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

The game ends when a player gets three marks in a row, column, or diagonal, or when all cells are filled and the game is a draw.

## How the AI Works

### 1. Breadth-First Search

The AI starts with the current board and explores legal moves one level at a time. Each search node contains:

- The board position.
- The mark whose turn it is.

The search records each unique **board-and-turn** combination once. If different move sequences lead to the same combination, the AI reuses the existing state instead of exploring it again. This reduces duplicate work while preserving all possible outcomes.

### 2. Minimax Evaluation

After building the reachable state graph, the AI evaluates states from the end of the game back toward the current position:

| Outcome          | Score |
| ---------------- | ----: |
| AI (`O`) wins    |   `1` |
| Human (`X`) wins |  `-1` |
| Draw             |   `0` |

On the AI's turn, Minimax chooses the highest-valued outcome. On the human's turn, it assumes the human will choose the lowest-valued outcome for the AI. The AI then selects the root move with the best score. This means it will choose a win when one is available, avoid a loss when possible, and otherwise accept a draw.

## Code Guide

### `WIN_LINES`

Stores the eight winning combinations as board indexes: three rows, three columns, and two diagonals. The `winner` function checks these combinations.

### `winner(board)`

Checks the board for a completed winning line.

- **Argument:** `board`, a sequence of nine cells containing `"X"`, `"O"`, or `" "` for an empty cell.
- **Returns:** The winning mark (`"X"` or `"O"`), or `None` if there is no winner.

### `other(player)`

Returns the other player's mark.

- **Argument:** `player`, either `"X"` or `"O"`.
- **Returns:** `"O"` when given `"X"`, or `"X"` when given `"O"`.

### `bfs_best_move(board, ai="O")`

Searches the game states reachable from the supplied board, evaluates them with Minimax, and selects the AI's best next move.

- **`board`:** A sequence containing exactly nine cells. Each cell must be `"X"`, `"O"`, or `" "`.
- **`ai`:** The mark used by the AI. It defaults to `"O"` and can also be set to `"X"`.
- **Returns:** A pair `(move_index, explored_state_count)`. `move_index` is an integer from `0` to `8`; `explored_state_count` is the number of unique states visited. If the board is already won or full, it returns `(None, 1)`.
- **Raises:** `ValueError` if the board has an invalid length or cell value, or if `ai` is not `"X"` or `"O"`.

This function expects a board where it is the AI's turn. It validates the board's shape and cell values, but does not verify that the board follows legal turn counts.

### `show(board)`

Prints the board in a readable 3 × 3 layout. Empty cells are displayed using their indexes so the player can choose them.

- **Argument:** `board`, the nine-cell game board.
- **Returns:** Nothing; it prints the board to the terminal.

### `play()`

Runs the interactive game loop. It creates an empty board, reads and validates the human's moves, asks the AI for its response, and prints the result when the game ends.

The final `if __name__ == "__main__":` block calls `play()` when the file is run directly. It also allows the functions to be imported from another Python file without automatically starting a game.

## Example: Calling the AI Function

You can use the AI function separately from the command-line game:

```python
from tic_tac_toe import bfs_best_move

board = [
    "X", "O", "X",
    " ", "O", " ",
    " ", " ", "X",
]

move, explored = bfs_best_move(board, ai="O")
print("AI move:", move)
print("Unique states explored:", explored)
```

The returned move is a board index. In this example, the AI is asked to move as `O` on the supplied board.

## Project File

- [`tic_tac_toe.py`](tic_tac_toe.py) — the complete game and AI implementation.
