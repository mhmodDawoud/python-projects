"""Uniform-Cost Search with a step-by-step frontier trace."""

import heapq
from itertools import count


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


def ucs(start, goal, graph, verbose=True):
    """Return the least-cost path and cost using Uniform-Cost Search.

    Graph values must be lists of (neighbor, non-negative_edge_cost) pairs.
    The insertion counter gives FIFO ordering to entries with equal costs.
    Returns (path, cost), or (None, None) when the goal is unreachable.
    """
    sequence = count()
    frontier = [(0, next(sequence), start, [start])]
    best_cost = {start: 0}
    expanded = []

    while frontier:
        cost, _, node, path = heapq.heappop(frontier)

        # Ignore an older queue entry if a cheaper route was found later.
        if cost != best_cost.get(node):
            continue

        expanded.append(node)
        if node == goal:
            if verbose:
                print("Expanded order:", expanded)
            return path, cost

        for neighbor, edge_cost in graph.get(node, []):
            if edge_cost < 0:
                raise ValueError("Uniform-Cost Search requires non-negative edge costs")

            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                new_path = path + [neighbor]
                heapq.heappush(
                    frontier,
                    (new_cost, next(sequence), neighbor, new_path),
                )

        if verbose:
            # Hide stale entries that no longer represent the best known route.
            current_frontier = sorted(
                (queued_cost, order, queued_node, queued_path)
                for queued_cost, order, queued_node, queued_path in frontier
                if queued_cost == best_cost.get(queued_node)
            )
            print(
                f"After expanding {node}:",
                [(queued_node, queued_cost) for queued_cost, _, queued_node, _ in current_frontier],
            )

    if verbose:
        print("Expanded order:", expanded)
    return None, None


def main():
    """Run the sample search from S to G and print its result."""
    path, cost = ucs("S", "G", GRAPH)
    print("Optimal path:", path)
    print("Total cost:", cost)


if __name__ == "__main__":
    main()