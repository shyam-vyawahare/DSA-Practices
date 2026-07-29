"""
Problem: Implement Queue using Stacks

Implement a First In First Out (FIFO) queue using only two stacks.

Implement the MyQueue class:
- push(x): Push element x to the back of the queue.
- pop(): Remove the element from the front of the queue and return it.
- peek(): Return the element at the front of the queue.
- empty(): Return True if the queue is empty, else False.

Example:
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output:
[null, null, null, 1, 1, False]

Technique: Two Stacks

Time Complexity:
- push()  : O(1)
- pop()   : Amortized O(1)
- peek()  : Amortized O(1)
- empty() : O(1)

Space Complexity: O(n)
"""


class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def _transfer(self):
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def pop(self) -> int:
        if not self.output_stack:
            self._transfer()
        return self.output_stack.pop()

    def peek(self) -> int:
        if not self.output_stack:
            self._transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


if __name__ == "__main__":
    queue = MyQueue()

    queue.push(10)
    queue.push(20)
    queue.push(30)

    print("Front:", queue.peek())       # 10
    print("Removed:", queue.pop())      # 10
    print("Front:", queue.peek())       # 20
    print("Is Empty?", queue.empty())   # False
