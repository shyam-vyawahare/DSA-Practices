"""
Problem: Subarray Sum Equals K
Technique: Prefix Sum + Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_map = {0: 1}

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_map:
                count += prefix_map[curr_sum - k]

            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

        return count
