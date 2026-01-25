"""
Problem: Subsets
Technique: Backtracking
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return

            # Include element
            path.append(nums[index])
            backtrack(index + 1, path)

            # Exclude element
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])
        return result
