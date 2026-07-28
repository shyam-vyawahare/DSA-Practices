"""
Topic: Queue Basics

A Queue is a linear data structure that follows the
FIFO (First In, First Out) principle.

Common Operations:
1. enqueue(item) -> Add an element to the rear
2. dequeue()     -> Remove and return the front element
3. front()       -> Return the front element without removing it
4. is_empty()    -> Check whether the queue is empty
5. size()        -> Return the number of elements

Time Complexity:
- Enqueue : O(1)
- Dequeue : O(1)
- Front   : O(1)
- Size    : O(1)

Space Complexity:
- O(n)
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()

    print("Enqueuing elements...")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Front element:", queue.front())
    print("Queue size:", queue.size())

    print("Dequeued:", queue.dequeue())
    print("Front after dequeue:", queue.front())

    print("Is queue empty?", queue.is_empty())
