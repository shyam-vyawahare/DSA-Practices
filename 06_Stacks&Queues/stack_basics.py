"""
Topic: Stack Basics

A Stack is a linear data structure that follows the
LIFO (Last In, First Out) principle.

Common Operations:
1. push(item)   -> Add an element to the top
2. pop()        -> Remove and return the top element
3. peek()       -> Return the top element without removing it
4. is_empty()   -> Check whether the stack is empty
5. size()       -> Return the number of elements

Time Complexity:
- Push : O(1)
- Pop  : O(1)
- Peek : O(1)
- Size : O(1)

Space Complexity:
- O(n)
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an element to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()

    print("Pushing elements...")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())
    print("Stack size:", stack.size())

    print("Popped:", stack.pop())
    print("Top after pop:", stack.peek())

    print("Is stack empty?", stack.is_empty())
