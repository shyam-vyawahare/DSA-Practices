"""
Problem: Contains Duplicate
Technique: Hash Set
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
