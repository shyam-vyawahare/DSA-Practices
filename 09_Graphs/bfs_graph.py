"""
Topic: Breadth-First Search (BFS)

BFS explores a graph level by level.

It uses a Queue following the FIFO
(First In, First Out) principle.

Example Graph:

    0 ---- 1
    |      |
    2 ---- 3
    |
    4

Starting from 0:
0 -> 1 -> 2 -> 3 -> 4

Time Complexity: O(V + E)
Space Complexity: O(V)

Where:
V = Number of vertices
E = Number of edges
"""

from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search starting from
    the given vertex.
    """

    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    traversal = []

    while queue:

        vertex = queue.popleft()
        traversal.append(vertex)

        for neighbor in graph[vertex]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


if __name__ == "__main__":

    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3, 4],
        3: [1, 2],
        4: [2]
    }

    start = 0

    result = bfs(graph, start)

    print("BFS Traversal:")
    print(result)
