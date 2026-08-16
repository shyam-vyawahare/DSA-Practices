"""
Problem: Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements.

Example:
Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]

Technique:
Hash Map + Min Heap

Time Complexity:
O(n log k)

Space Complexity:
O(n)
"""

import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count the frequency of each number.
        frequency = Counter(nums)

        # Min Heap storing:
        # (frequency, number)
        min_heap = []

        for num, count in frequency.items():

            heapq.heappush(min_heap, (count, num))

            # Keep only the k most frequent elements.
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract elements from the heap.
        return [num for count, num in min_heap]


if __name__ == "__main__":

    solution = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    result = solution.topKFrequent(nums, k)

    print("Array:", nums)
    print("K:", k)
    print("Top K Frequent Elements:", result)
