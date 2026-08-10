"""
Topic: Heap Basics

A Heap is a complete binary tree commonly used to implement
Priority Queues.

Types:
1. Min Heap -> Smallest element at the root
2. Max Heap -> Largest element at the root

Python's heapq module provides a Min Heap.

Common Operations:
- Push      : O(log n)
- Pop       : O(log n)
- Peek      : O(1)
- Heapify   : O(n)

Space Complexity:
- O(n)
"""

import heapq


# -----------------------------
# Min Heap
# -----------------------------

min_heap = []

heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)

print("Min Heap:", min_heap)

print("Smallest element:", min_heap[0])

print("Removed:", heapq.heappop(min_heap))

print("Min Heap after pop:", min_heap)


# -----------------------------
# Heapify
# -----------------------------

numbers = [20, 5, 15, 30, 10]

heapq.heapify(numbers)

print("\nHeapified list:", numbers)

print("Smallest element:", numbers[0])


# -----------------------------
# Max Heap
# -----------------------------

# Python does not provide a direct Max Heap.
# We can simulate one by storing negative values.

max_heap = []

for number in [30, 10, 20, 5]:
    heapq.heappush(max_heap, -number)

print("\nMax Heap:", [-x for x in max_heap])

largest = -heapq.heappop(max_heap)

print("Largest element:", largest)
