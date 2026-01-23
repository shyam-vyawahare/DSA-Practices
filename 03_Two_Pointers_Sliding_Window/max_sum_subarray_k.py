"""
Problem: Maximum Sum Subarray of Size K
Technique: Fixed Sliding Window
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxSumSubarray(self, nums: List[int], k: int) -> int:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum
