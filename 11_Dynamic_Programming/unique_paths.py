"""
Unique Paths

Problem:
Given an m x n grid, find the number of unique paths from
the top-left corner to the bottom-right corner.

You can only move right or down.

Example:
m = 3
n = 3

Output:
6
"""


def unique_paths(m, n):
    """
    Calculate the number of unique paths using
    bottom-up dynamic programming.
    """

    # dp[j] represents the number of ways to reach
    # the current cell in column j.
    dp = [1] * n

    # Process each row after the first row.
    for _ in range(1, m):

        for j in range(1, n):
            # Ways to reach current cell =
            # ways from above + ways from left
            dp[j] = dp[j] + dp[j - 1]

    return dp[n - 1]


# Example 1
m = 3
n = 3

print("Grid:", m, "x", n)
print("Unique Paths:", unique_paths(m, n))


# Example 2
m = 3
n = 7

print("\nGrid:", m, "x", n)
print("Unique Paths:", unique_paths(m, n))
