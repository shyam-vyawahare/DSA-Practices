"""
Problem: Number of Connected Components in an Undirected Graph

You have n nodes labeled from 0 to n - 1.

You are given an array of edges where:
edges[i] = [a, b]

means there is an undirected edge between nodes a and b.

Return the number of connected components in the graph.

Example:

Input:
n = 5
edges = [[0, 1], [1, 2], [3, 4]]

Graph:

    0 --- 1 --- 2

    3 --- 4

Output:
2

Technique:
DFS + Visited Set

Time Complexity:
O(V + E)

Space Complexity:
O(V + E)

Where:
V = Number of vertices
E = Number of edges
"""

from typing import List


class Solution:

    def countComponents(
        self,
        n: int,
        edges: List[List[int]]
    ) -> int:

        # Build adjacency list.
        graph = [[] for _ in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        components = 0

        def dfs(node):
            """Visit every node in the current component."""

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Every unvisited node starts a new component.
        for node in range(n):

            if node not in visited:
                components += 1
                dfs(node)

        return components


if __name__ == "__main__":

    solution = Solution()

    n = 5
    edges = [
        [0, 1],
        [1, 2],
        [3, 4]
    ]

    result = solution.countComponents(n, edges)

    print("Number of Connected Components:", result)
