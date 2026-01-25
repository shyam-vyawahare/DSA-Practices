"""
Problem: Combination Sum
Technique: Backtracking
Time Complexity: Exponential
Space Complexity: O(target)
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target or index == len(candidates):
                return

            # Pick current
            backtrack(index, path + [candidates[index]], total + candidates[index])

            # Skip current
            backtrack(index + 1, path, total)

        backtrack(0, [], 0)
        return result
