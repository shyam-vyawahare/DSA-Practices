"""
Topic: Priority Queue

A Priority Queue is a data structure where each element is
processed according to its priority rather than simply
following insertion order.

Python's heapq module can be used to implement a Min Priority Queue.

Lower priority number = Higher priority

Example:
Priority 1 -> Process first
Priority 2 -> Process second
Priority 3 -> Process third

Operations:
- Insert / Push : O(log n)
- Remove / Pop  : O(log n)
- Peek          : O(1)

Space Complexity: O(n)
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, value):
        """
        Add an element with a given priority.

        Lower priority number is processed first.
        """
        heapq.heappush(self.queue, (priority, value))

    def pop(self):
        """Remove and return the highest-priority element."""
        if not self.queue:
            raise IndexError("Pop from an empty priority queue")

        priority, value = heapq.heappop(self.queue)
        return priority, value

    def peek(self):
        """Return the highest-priority element without removing it."""
        if not self.queue:
            raise IndexError("Peek from an empty priority queue")

        return self.queue[0]

    def is_empty(self):
        """Check whether the priority queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements."""
        return len(self.queue)


if __name__ == "__main__":

    pq = PriorityQueue()

    pq.push(3, "Low Priority Task")
    pq.push(1, "Critical Task")
    pq.push(2, "Normal Task")

    print("Highest Priority:", pq.peek())

    print("Processing:", pq.pop())
    print("Processing:", pq.pop())
    print("Processing:", pq.pop())

    print("Is Empty:", pq.is_empty())
