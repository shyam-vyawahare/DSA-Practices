"""
Problem: Generate Parentheses
Technique: Backtracking
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open_count, close_count, path):
            if open_count == close_count == n:
                result.append(path)
                return

            if open_count < n:
                backtrack(open_count + 1, close_count, path + "(")

            if close_count < open_count:
                backtrack(open_count, close_count + 1, path + ")")

        backtrack(0, 0, "")
        return result
