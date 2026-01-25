"""
Problem: Factorial of a Number
Technique: Recursion
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
