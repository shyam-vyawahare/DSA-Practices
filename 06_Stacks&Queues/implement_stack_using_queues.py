"""
Problem: Implement Stack using Queues

Implement a Last In First Out (LIFO) stack using only queues.

Implement the MyStack class:
- push(x): Push element x onto the stack.
- pop(): Remove the element on the top of the stack and return it.
- top(): Return the top element.
- empty(): Return True if the stack is empty, else False.

Example:
Input:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output:
[null, null, null, 2, 2, False]

Technique: Queue Rotation

Time Complexity:
- push() : O(n)
- pop()  : O(1)
- top()  : O(1)
- empty(): O(1)

Space Complexity: O(n)
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        # Rotate the queue so the newly added element
        # comes to the front.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == "__main__":
    stack = MyStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top:", stack.top())          # 30
    print("Popped:", stack.pop())       # 30
    print("Top:", stack.top())          # 20
    print("Is Empty?", stack.empty())   # False
