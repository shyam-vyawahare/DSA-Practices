"""
Climbing Stairs

You are climbing a staircase with n steps.

At each step, you can climb either 1 step or 2 steps.

Return the number of distinct ways to reach the top.

DP Pattern:
    1D Dynamic Programming

Recurrence:
    dp[i] = dp[i - 1] + dp[i - 2]

Time Complexity:
    O(n)

Space Complexity:
    O(1) for the optimized solution.
"""


def climb_stairs(n):
    """
    Return the number of distinct ways to reach
    the top of a staircase with n steps.

    Args:
        n: Number of stairs.

    Returns:
        Number of distinct ways.
    """

    # Base cases.
    if n <= 2:
        return n

    # Number of ways to reach the previous two steps.
    previous = 1
    current = 2

    for _ in range(3, n + 1):
        next_ways = previous + current

        previous = current
        current = next_ways

    return current


if __name__ == "__main__":
    n = 5

    result = climb_stairs(n)

    print("Number of ways:", result)
