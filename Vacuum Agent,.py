import random
import time

# D = pillar, * = dirt, V = vacuum
directions = [
    [" ", "D", "*"],
    ["D", " ", " "],
    ["*", " ", "D"],
]

# ===== your code: finds the D positions =====
def get_index(directions):
    indexes = []
    for row_index, row in enumerate(directions):
        for column_index, column in enumerate(row):
            if column == "D":
                indexes.append((row_index, column_index))
    return indexes

# ===== is there any dirt left? =====
def has_dirt(grid):
    for row in grid:
        for cell in row:
            if cell == "*":
                return True
    return False

# ===== where can the vacuum move? (not outside the grid, not onto D) =====
def get_moves(grid, r, c):
    moves = []
    if r > 0 and grid[r - 1][c] != "D":
        moves.append("up")
    if r < 2 and grid[r + 1][c] != "D":
        moves.append("down")
    if c > 0 and grid[r][c - 1] != "D":
        moves.append("left")
    if c < 2 and grid[r][c + 1] != "D":
        moves.append("right")
    return moves

# ===== print the grid in the SAME place (clear the screen first) =====
def show(grid):
    print("\033[H\033[J", end="")
    for row in grid:
        print(row)

# ===== main program =====
r = 1                       # vacuum starts in the middle
c = 1
directions[r][c] = "V"
show(directions)

while has_dirt(directions):
    time.sleep(0.5)

    moves = get_moves(directions, r, c)
    move = random.choice(moves)      # pick a random move

    directions[r][c] = " "           # leave the old cell

    if move == "up":
        r = r - 1
    elif move == "down":
        r = r + 1
    elif move == "left":
        c = c - 1
    else:
        c = c + 1

    directions[r][c] = "V"           # enter the new cell (dirt gets cleaned)
    show(directions)

print("All clean!")