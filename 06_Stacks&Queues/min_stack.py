"""
Problem: Min Stack

Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

Implement the MinStack class:
- push(val): Push the element onto the stack.
- pop(): Remove the top element.
- top(): Get the top element.
- getMin(): Retrieve the minimum element.

Example:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Technique: Auxiliary Stack

Time Complexity:
- push()   : O(1)
- pop()    : O(1)
- top()    : O(1)
- getMin() : O(1)

Space Complexity: O(n)
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    min_stack = MinStack()

    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    print("Minimum:", min_stack.getMin())   # -3

    min_stack.pop()

    print("Top:", min_stack.top())          # 0
    print("Minimum:", min_stack.getMin())   # -2
