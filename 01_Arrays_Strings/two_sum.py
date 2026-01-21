"""
Problem: Two Sum
Technique: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in lookup:
                return [lookup[complement], index]
            lookup[value] = index
