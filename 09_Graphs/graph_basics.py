"""
Topic: Graph Basics

A Graph is a non-linear data structure consisting of:

- Vertices (Nodes)
- Edges (Connections)

Example:

    0 ---- 1
    |      |
    |      |
    2 ---- 3

Vertices: 0, 1, 2, 3
Edges: (0,1), (0,2), (1,3), (2,3)

Types of Graphs:
1. Directed Graph
2. Undirected Graph
3. Weighted Graph
4. Unweighted Graph

Important Terms:
- Vertex / Node
- Edge
- Degree
- Path
- Cycle
- Connected Component

Graph Traversal:
- BFS -> Breadth-First Search
- DFS -> Depth-First Search

Time Complexity:
Depends on representation and algorithm.

For an adjacency list:
Traversal -> O(V + E)

Where:
V = Number of vertices
E = Number of edges

Space Complexity:
O(V + E)
"""


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an undirected edge between two vertices."""

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        """Display the graph."""

        for vertex in self.adjacency_list:
            print(
                f"{vertex} -> "
                f"{self.adjacency_list[vertex]}"
            )


if __name__ == "__main__":

    graph = Graph()

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

    print("Graph:")
    graph.display()
