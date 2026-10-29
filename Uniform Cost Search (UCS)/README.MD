# Uniform-Cost Search (UCS)

A Python example of **Uniform-Cost Search**, a graph-search algorithm that finds a least-cost path from a start node to a goal node. The program searches the sample weighted graph from `S` to `G` and prints the expansion order, frontier after each expansion, best path, and total path cost.

## Features

- Uses Python's `heapq` priority queue to expand the lowest-cost candidate first.
- Uses a sequence counter to process equal-cost candidates in first-in, first-out order.
- Tracks the best known cost to each node and skips outdated, more expensive queue entries.
- Prints a readable frontier trace while searching.
- Handles unreachable goals and rejects negative edge costs.
- Uses only the Python standard library.

## Requirements

- Python 3
- No third-party packages are required.

## Run the Example

Open a terminal in the folder containing `uniform_cost_search.py` and run:

```bash
python uniform_cost_search.py
```

If your system uses `python3` as the Python command, run:

```bash
python3 uniform_cost_search.py
```

## Sample Graph

The graph is represented as an adjacency list. Each node maps to a list of `(neighbor, edge_cost)` pairs:

```python
GRAPH = {
    "S": [("A", 2), ("B", 5)],
    "A": [("C", 4), ("D", 1)],
    "B": [("E", 2), ("F", 6)],
    "C": [("G", 3)],
    "D": [("G", 2)],
    "E": [("G", 4)],
    "F": [("G", 1)],
    "G": [],
}
```

For example, `("A", 2)` means there is an edge from `S` to `A` with a cost of `2`.

## How UCS Works

1. Add the start node to a priority queue with total cost `0`.
2. Remove the queued path with the lowest total cost.
3. If its node is the goal, return that path and cost. With non-negative edge costs, the first time the goal is removed from the queue, its path has the minimum total cost.
4. Otherwise, add each neighbor if this route improves the best cost known for that neighbor.
5. Continue until the goal is found or the queue is empty.

The insertion counter is the second priority-queue field. It breaks equal-cost ties in FIFO order and prevents Python from needing to compare node labels or path lists.

The best-cost table avoids unnecessary work. If a node is first reached by an expensive path and later found by a cheaper one, the cheaper route replaces it. The old queue entry is ignored when it is eventually removed.

## Sample Result

The least-cost path from `S` to `G` is:

```text
S -> A -> D -> G
```

Its total cost is `2 + 1 + 2 = 5`. In the sample run, the expanded order is `S, A, D, B, G`; `B` is expanded before `G` because both have total cost `5`, and `B` entered the queue first.

## Function Guide

### `ucs(start, goal, graph, verbose=True)`

Finds a least-cost path using Uniform-Cost Search.

- **`start`**: The node where the search begins.
- **`goal`**: The destination node to find.
- **`graph`**: A dictionary mapping each node to a list of `(neighbor, edge_cost)` pairs. All edge costs must be non-negative.
- **`verbose`**: When `True` (the default), prints the expanded order and the useful frontier entries after each expansion. Set it to `False` to run silently.
- **Returns:** `(path, cost)`, where `path` is a list of nodes and `cost` is the total path cost. Returns `(None, None)` if no path to the goal exists.
- **Raises:** `ValueError` if a negative edge cost is encountered.

Nodes without an entry in the graph are treated as having no outgoing edges.

### `main()`

Runs the sample search from `S` to `G`, then prints the path and total cost.

The `if __name__ == "__main__":` block calls `main()` when the file is run directly. Importing the module does not automatically start the sample search.

## Use UCS with Another Graph
