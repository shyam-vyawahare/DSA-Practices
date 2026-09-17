"""
Dynamic Programming - Fundamentals

This file demonstrates different approaches to solving
the Fibonacci sequence:

1. Plain Recursion
2. Memoization (Top-Down DP)
3. Tabulation (Bottom-Up DP)
4. Space-Optimized DP

The purpose is to understand why Dynamic Programming
can significantly improve recursive solutions.
"""


# ---------------------------------------------------------
# 1. Plain Recursion
# ---------------------------------------------------------

def fibonacci_recursive(n):
    """
    Calculate Fibonacci using plain recursion.

    Time Complexity:
        O(2^n)

    Space Complexity:
        O(n)
    """

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ---------------------------------------------------------
# 2. Memoization - Top-Down DP
# ---------------------------------------------------------

def fibonacci_memoization(n, memo=None):
    """
    Calculate Fibonacci using recursion + memoization.

    Memoization stores already calculated results so that
    the same subproblem is never solved more than once.

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """

    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = (
        fibonacci_memoization(n - 1, memo)
        + fibonacci_memoization(n - 2, memo)
    )

    return memo[n]


# ---------------------------------------------------------
# 3. Tabulation - Bottom-Up DP
# ---------------------------------------------------------

def fibonacci_tabulation(n):
    """
    Calculate Fibonacci using bottom-up tabulation.

    Instead of starting from n and going downward,
    we build the solution from the smallest subproblems.

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """

    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ---------------------------------------------------------
# 4. Space-Optimized Dynamic Programming
# ---------------------------------------------------------

def fibonacci_optimized(n):
    """
    Calculate Fibonacci using constant extra space.

    We only need the previous two Fibonacci values,
    so storing the entire DP array is unnecessary.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)
    """

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        next_value = previous + current

        previous = current
        current = next_value

    return current


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    n = 10

    print("Fibonacci using recursion:")
    print(fibonacci_recursive(n))

    print("\nFibonacci using memoization:")
    print(fibonacci_memoization(n))

    print("\nFibonacci using tabulation:")
    print(fibonacci_tabulation(n))

    print("\nFibonacci using space-optimized DP:")
    print(fibonacci_optimized(n))
