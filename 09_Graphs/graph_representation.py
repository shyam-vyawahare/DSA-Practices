"""
Topic: Graph Representation

Graphs can commonly be represented using:

1. Adjacency List
2. Adjacency Matrix

Adjacency List:
- Stores each vertex along with its neighboring vertices.
- Efficient for sparse graphs.

Space Complexity: O(V + E)

Adjacency Matrix:
- Uses a 2D matrix.
- matrix[i][j] indicates whether an edge exists
  between vertex i and vertex j.

Space Complexity: O(V^2)

Where:
V = Number of vertices
E = Number of edges
"""


# ==========================================
# 1. Adjacency List
# ==========================================

class GraphList:

    def __init__(self, vertices):
        self.graph = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, vertex1, vertex2):
        """Add an undirected edge."""
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")


# ==========================================
# 2. Adjacency Matrix
# ==========================================

class GraphMatrix:

    def __init__(self, vertices):
        self.matrix = [
            [0] * vertices
            for _ in range(vertices)
        ]

    def add_edge(self, vertex1, vertex2):
        """Add an undirected edge."""
        self.matrix[vertex1][vertex2] = 1
        self.matrix[vertex2][vertex1] = 1

    def display(self):
        for row in self.matrix:
            print(row)


# ==========================================
# Example
# ==========================================

if __name__ == "__main__":

    vertices = 4

    # -------- Adjacency List --------

    print("Adjacency List:")

    graph_list = GraphList(vertices)

    graph_list.add_edge(0, 1)
    graph_list.add_edge(0, 2)
    graph_list.add_edge(1, 3)
    graph_list.add_edge(2, 3)

    graph_list.display()

    # -------- Adjacency Matrix --------

    print("\nAdjacency Matrix:")

    graph_matrix = GraphMatrix(vertices)

    graph_matrix.add_edge(0, 1)
    graph_matrix.add_edge(0, 2)
    graph_matrix.add_edge(1, 3)
    graph_matrix.add_edge(2, 3)

    graph_matrix.display()
