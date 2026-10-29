# Tree Search: DFS and Depth-Limited Search

This Python program demonstrates two ways to search a tree or graph:

- **Depth-First Search (DFS)** explores one branch as far as it can before returning to explore another branch.
- **Depth-Limited Search (DLS)** works like DFS but stops exploring a branch after a specified depth.

The included example searches for node `H`, starting at node `A`.

## Requirements

- Python 3
- No third-party packages are required.

## Run the Example

Open a terminal in the folder containing `tree_search.py` and run:

```bash
python tree_search.py
```

If your system uses `python3` as the Python command, run:

```bash
python3 tree_search.py
```

## Sample Tree

The graph is stored as an adjacency list: each node maps to the list of its children.

```text
        A
       / \
      B   C
     / \ / \
    D  E F  G
       |
       H
```

The `TREE` dictionary defines the same structure:

```python
TREE = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": [],
}
```

Children are visited in the order listed. In this example, `B` is explored before `C`, and `D` before `E`.

## Search Behavior

### Depth-First Search

DFS uses a stack. It removes the most recently added node, then pushes that node's children onto the stack. Children are pushed in reverse order so that the leftmost child is visited first.

For a search from `A` to `H`, the visit order is:

```text
A, B, D, E, H
```

The path returned is:

```text
A -> B -> E -> H
```

DFS keeps a set of visited nodes so it does not process the same node more than once. This also helps it safely search graphs that contain shared nodes or cycles.

### Depth-Limited Search

DLS is recursive DFS with a maximum depth. The starting node has depth `0`; each edge followed increases the depth by `1`.

For the sample tree:

- With a limit of `2`, DLS cannot reach `H`, which is at depth `3`.
- With a limit of `3`, DLS reaches `H` and returns the path `A -> B -> E -> H`.

DLS tracks nodes visited during the search. It also avoids following a node that already appears on the current path, which prevents an infinite loop if the graph contains a cycle. The depth limit applies separately to each search path.

## Functions

### `dfs(start, goal, graph)`

Performs iterative Depth-First Search.
