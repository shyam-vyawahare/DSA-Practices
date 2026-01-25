"""
Problem: Permutations
Technique: Backtracking
Time Complexity: O(n!)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return

            for i in range(len(remaining)):
                backtrack(
                    path + [remaining[i]],
                    remaining[:i] + remaining[i + 1:]
                )

        backtrack([], nums)
        return result
