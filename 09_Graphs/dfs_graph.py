"""
Topic: Depth-First Search (DFS)

DFS explores a graph by going as deep as possible along
each branch before backtracking.

DFS can be implemented using:
1. Recursion
2. Explicit Stack

This file demonstrates the recursive approach.

Example Graph:

    0 ---- 1
    |      |
    2 ---- 3
    |
    4

Starting from 0:
0 -> 1 -> 3 -> 2 -> 4

Time Complexity: O(V + E)
Space Complexity: O(V)

Where:
V = Number of vertices
E = Number of edges
"""

from typing import Dict, List, Set


def dfs(
    graph: Dict[int, List[int]],
    vertex: int,
    visited: Set[int],
    traversal: List[int]
) -> None:
    """
    Perform Depth-First Search recursively.
    """

    # Mark the current vertex as visited.
    visited.add(vertex)

    # Add it to the traversal result.
    traversal.append(vertex)

    # Visit each unvisited neighbor.
    for neighbor in graph[vertex]:

        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)


if __name__ == "__main__":

    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3, 4],
        3: [1, 2],
        4: [2]
    }

    start = 0

    visited = set()
    traversal = []

    dfs(graph, start, visited, traversal)

    print("DFS Traversal:")
    print(traversal)
