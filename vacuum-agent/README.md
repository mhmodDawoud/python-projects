# Vacuum Agent

A small Python program that simulates a vacuum cleaner moving randomly inside a 3x3 room until all the dirt is cleaned.

## What is in the room?

| Symbol      | Meaning                               |
| ----------- | ------------------------------------- |
| `V`         | The vacuum                            |
| `D`         | A pillar (the vacuum cannot enter it) |
| `*`         | Dirt                                  |
| ` ` (space) | Empty cell                            |

The starting room looks like this:

```
[' ', 'D', '*']
['D', ' ', ' ']
['*', ' ', 'D']
```

## How it works

1. `get_index` finds the positions of all the pillars (`D`) in the room.
2. `has_dirt` checks if there is any dirt (`*`) left.
3. `get_moves` finds where the vacuum can move: not outside the room and not onto a pillar.
4. The main loop repeats these steps until there is no dirt left:
   - Pick a random move from the allowed moves.
   - Leave the old cell.
   - Move to the new cell (if it has dirt, the dirt is cleaned).
   - Redraw the room in the same place on the screen.
5. When all the dirt is gone, the program prints `All clean!`.

## How to run

1. Install Python 3.
2. Save the code in a file, for example `vacuum.py`.
3. Open a terminal in the same folder and run:

```
python vacuum.py
```

> Note: the screen-clearing animation works in a normal terminal or VS Code, but not in IDLE.

## Example output

The room updates in the same place after every move:

```
[' ', 'D', '*']
['D', 'V', ' ']
['*', ' ', 'D']
```

and at the end:

```
All clean!
```

## Ideas to improve it

- Count how many steps the vacuum takes.
- Add more dirt or change the places of the pillars.
- Make the vacuum go to the nearest dirt instead of moving randomly.

## Important

Every dirt cell must be reachable. If a `*` is surrounded by pillars or walls, the program will never finish.
