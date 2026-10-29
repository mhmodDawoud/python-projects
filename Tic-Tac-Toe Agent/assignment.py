from collections import deque


WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def winner(board):
    """Return the winning mark, or None when the game has no winner."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def other(player):
    """Return the opponent's mark."""
    return "O" if player == "X" else "X"


def bfs_best_move(board, ai="O"):
    """Find an optimal move by BFS exploration and minimax evaluation.

    Repeated board-and-turn states are stored once, reducing the search from
    exploring duplicate move sequences to exploring unique game states.
    Returns (move_index, number_of_unique_states_explored).
    """
    if len(board) != 9 or any(cell not in ("X", "O", " ") for cell in board):
        raise ValueError("board must contain exactly 9 cells with X, O, or spaces")
    if ai not in ("X", "O"):
        raise ValueError("ai must be 'X' or 'O'")

    root_board = tuple(board)
    if winner(root_board) or " " not in root_board:
        return None, 1

    # Each node stores a board and the player whose turn it is.
    nodes = [(root_board, ai)]
    state_to_index = {(root_board, ai): 0}
    children = {}
    queue = deque([0])

    # Explore each distinct state once, one BFS level at a time.
    while queue:
        index = queue.popleft()
        current_board, player = nodes[index]

        if winner(current_board) or " " not in current_board:
            continue

        for move, cell in enumerate(current_board):
            if cell != " ":
                continue

            next_board = list(current_board)
            next_board[move] = player
            next_state = (tuple(next_board), other(player))

            child_index = state_to_index.get(next_state)
            if child_index is None:
                child_index = len(nodes)
                state_to_index[next_state] = child_index
                nodes.append(next_state)
                queue.append(child_index)

            # Keep the move alongside the edge for selecting the root move.
            children.setdefault(index, []).append((child_index, move))

    # Evaluate states from the leaves back to the root using minimax.
    values = [0] * len(nodes)
    for index in range(len(nodes) - 1, -1, -1):
        current_board, player = nodes[index]
        result = winner(current_board)

        if result == ai:
            values[index] = 1
        elif result is not None:
            values[index] = -1
        elif index not in children:
            values[index] = 0
        else:
            child_values = [values[child] for child, _ in children[index]]
            values[index] = max(child_values) if player == ai else min(child_values)

    best_child, best_move = max(children[0], key=lambda edge: values[edge[0]])
    return best_move, len(nodes)


def show(board):
    """Print the board with cell indexes shown for empty squares."""
    for row in range(3):
        cells = [board[row * 3 + col] for col in range(3)]
        print(" | ".join(cell if cell != " " else str(row * 3 + col) for col, cell in enumerate(cells)))
        if row < 2:
            print("---------")
    print()


def play():
    board = [" "] * 9
    human, ai = "X", "O"
    show(board)

    while True:
        try:
            move = int(input("Choose a cell (0-8): "))
        except ValueError:
            print("Please enter a number from 0 to 8.")
            continue

        if not 0 <= move < 9:
            print("Choose a number from 0 to 8.")
            continue
        if board[move] != " ":
            print("That cell is already occupied.")
            continue

        board[move] = human
        if winner(board) or " " not in board:
            break

        move, explored = bfs_best_move(board, ai)
        print(f"AI explored {explored} unique states and plays {move}.")
        board[move] = ai
        show(board)

        if winner(board) or " " not in board:
            break

    show(board)
    print("Winner:", winner(board) or "Draw")


if __name__ == "__main__":
    play()