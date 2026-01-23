"""
Problem: Remove Duplicates from Sorted Array
Technique: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
