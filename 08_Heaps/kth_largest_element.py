"""
Problem: Kth Largest Element in an Array

Given an integer array nums and an integer k,
return the kth largest element in the array.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Technique: Min Heap

Time Complexity: O(n log k)
Space Complexity: O(k)

Idea:
Maintain a Min Heap containing only the k largest elements.

The smallest element in this heap will be the
kth largest element overall.
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # Keep only k largest elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


if __name__ == "__main__":

    solution = Solution()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    result = solution.findKthLargest(nums, k)

    print("Array:", nums)
    print("K:", k)
    print("Kth Largest:", result)
