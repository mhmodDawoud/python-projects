"""Depth-First Search and Depth-Limited Search on a sample tree."""


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


def dfs(start, goal, graph):
    """Return the nodes visited and the first DFS path to the goal.

    Children are explored from left to right according to their order in the
    graph. Returns (visited_nodes, path), or (visited_nodes, None) if absent.
    """
    stack = [(start, [start])]
    visited = []
    visited_set = set()

    while stack:
        node, path = stack.pop()
        if node in visited_set:
            continue

        visited.append(node)
        visited_set.add(node)

        if node == goal:
            return visited, path

        # Push children in reverse so the leftmost child is processed first.
        for child in reversed(graph.get(node, [])):
            if child not in visited_set:
                stack.append((child, path + [child]))

    return visited, None


def dls(node, goal, limit, graph, path=None, visited=None):
    """Run recursive Depth-Limited Search and return a path if found.

    The start node is at depth 0. ``visited`` records nodes in their
    exploration order. Returns None when the goal is not found within limit.
    """
    if limit < 0:
        raise ValueError("limit must be zero or greater")

    if path is None:
        path = [node]
    if visited is None:
        visited = []

    visited.append(node)

    if node == goal:
        return path
    if limit == 0:
        return None

    for child in graph.get(node, []):
        # Avoid looping if the input graph contains a cycle on the current path.
        if child in path:
            continue

        result = dls(
            child,
            goal,
            limit - 1,
            graph,
            path + [child],
            visited,
        )
        if result is not None:
            return result

    return None


def main():
    """Run the sample searches and print their visited nodes and paths."""
    visited, path = dfs("A", "H", TREE)
    print("DFS visited nodes:", visited)
    print("DFS path to H:", path)
    print()

    for limit in (2, 3):
        visited = []
        result = dls("A", "H", limit, TREE, visited=visited)
        print(f"DLS with limit={limit}")
        print("  Visited nodes:", visited)
        print("  Path:", result if result is not None else "Cutoff (goal not found)")
        print()


if __name__ == "__main__":
    main()