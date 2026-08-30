"""
Problem: Clone Graph

Given a reference to a node in a connected undirected graph,
return a deep copy (clone) of the graph.

Each node contains:
- val   -> Integer value
- neighbors -> List of neighboring nodes

Example:

    1 ----- 2
    |       |
    |       |
    4 ----- 3

Input:
A reference to node 1

Output:
A completely independent copy of the graph.

Technique:
DFS + Hash Map

Time Complexity:
O(V + E)

Space Complexity:
O(V)

Where:
V = Number of vertices
E = Number of edges
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if node is None:
            return None

        # Maps original nodes to their cloned nodes.
        clones = {}

        def dfs(current):

            # Return existing clone if this node
            # has already been processed.
            if current in clones:
                return clones[current]

            # Create a clone of the current node.
            clone = Node(current.val)

            # Store it before visiting neighbors.
            # This prevents infinite recursion for cycles.
            clones[current] = clone

            # Clone every neighbor.
            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


def print_graph(node, visited=None):
    """Print the graph using DFS."""

    if node is None:
        return

    if visited is None:
        visited = set()

    if node in visited:
        return

    visited.add(node)

    print(
        f"{node.val} -> "
        f"{[neighbor.val for neighbor in node.neighbors]}"
    )

    for neighbor in node.neighbors:
        print_graph(neighbor, visited)


if __name__ == "__main__":

    # Create graph:
    #
    #     1 ----- 2
    #     |       |
    #     |       |
    #     4 ----- 3

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()

    cloned_graph = solution.cloneGraph(node1)

    print("Original Graph:")
    print_graph(node1)

    print("\nCloned Graph:")
    print_graph(cloned_graph)
