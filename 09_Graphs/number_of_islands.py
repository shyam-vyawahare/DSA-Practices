"""
Problem: Number of Islands

Given an m x n 2D binary grid where:
- '1' represents land
- '0' represents water

An island is formed by connecting adjacent lands
horizontally or vertically.

Return the number of islands.

Example:

Input:
[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "1", "0"],
    ["0", "0", "0", "1", "1"],
    ["0", "0", "0", "0", "0"]
]

Output:
2

Technique:
DFS + Grid Traversal

Time Complexity:
O(m * n)

Space Complexity:
O(m * n) in the worst case due to recursion.

Note:
Each cell is visited at most once.
"""

from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(row, col):
            # Stop if outside the grid.
            if row < 0 or row >= rows:
                return

            if col < 0 or col >= cols:
                return

            # Stop if the cell is water.
            if grid[row][col] == "0":
                return

            # Mark this land cell as visited.
            grid[row][col] = "0"

            # Explore four directions.
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col + 1)  # Right
            dfs(row, col - 1)  # Left

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1":
                    islands += 1

                    # Explore the entire island.
                    dfs(row, col)

        return islands


if __name__ == "__main__":

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "1", "0"],
        ["0", "0", "0", "1", "1"],
        ["0", "0", "0", "0", "0"]
    ]

    solution = Solution()

    result = solution.numIslands(grid)

    print("Number of Islands:", result)
