"""
Problem: Intersection of Two Arrays
Technique: Hash Set
Time Complexity: O(n + m)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()

        for num in nums2:
            if num in set1:
                result.add(num)

        return list(result)
