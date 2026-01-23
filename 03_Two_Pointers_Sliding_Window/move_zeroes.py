"""
Problem: Move Zeroes
Technique: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
