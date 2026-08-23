"""
Problem: Find Median from Data Stream

Design a data structure that supports:

1. addNum(num)
   Add an integer to the data structure.

2. findMedian()
   Return the median of all elements so far.

Example:

Input:
5
15
1
3

After adding:
[5]           -> Median = 5
[5, 15]       -> Median = 10.0
[1, 5, 15]    -> Median = 5
[1, 3, 5, 15] -> Median = 4.0

Technique:
Two Heaps

- Max Heap -> Stores the smaller half
- Min Heap -> Stores the larger half

Time Complexity:
addNum()    -> O(log n)
findMedian() -> O(1)

Space Complexity:
O(n)
"""

import heapq


class MedianFinder:

    def __init__(self):
        # Max Heap for the smaller half.
        # Python has only Min Heap, so we store negative values.
        self.small = []

        # Min Heap for the larger half.
        self.large = []

    def addNum(self, num: int) -> None:

        # Add the number to the Max Heap.
        heapq.heappush(self.small, -num)

        # Make sure every value in small <= every value in large.
        if self.small and self.large:
            if -self.small[0] > self.large[0]:
                small_value = -heapq.heappop(self.small)
                large_value = heapq.heappop(self.large)

                heapq.heappush(self.small, -large_value)
                heapq.heappush(self.large, small_value)

        # Balance the sizes.
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:

        # Odd number of elements.
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        if len(self.large) > len(self.small):
            return float(self.large[0])

        # Even number of elements.
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":

    median_finder = MedianFinder()

    numbers = [5, 15, 1, 3]

    for number in numbers:
        median_finder.addNum(number)

        print(
            f"Added {number} -> "
            f"Median: {median_finder.findMedian()}"
  )
