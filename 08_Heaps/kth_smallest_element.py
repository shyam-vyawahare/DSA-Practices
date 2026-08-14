"""
Problem: Kth Smallest Element in an Array

Given an integer array nums and an integer k,
return the kth smallest element in the array.

Example:
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 2

Input: nums = [7, 10, 4, 3, 20, 15], k = 3
Output: 7

Technique: Max Heap

Time Complexity: O(n log k)
Space Complexity: O(k)

Idea:
Maintain a Max Heap containing only the k smallest elements.

The largest element in this heap will be the
kth smallest element overall.
"""

import heapq
from typing import List


class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:

        max_heap = []

        for num in nums:

            # Python provides a Min Heap,
            # so store negative values to simulate Max Heap.
            heapq.heappush(max_heap, -num)

            # Keep only k smallest elements.
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Convert the negative value back.
        return -max_heap[0]


if __name__ == "__main__":

    solution = Solution()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    result = solution.findKthSmallest(nums, k)

    print("Array:", nums)
    print("K:", k)
    print("Kth Smallest:", result)
