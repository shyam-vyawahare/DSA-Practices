"""
Problem: Valid Parentheses

Given a string s containing only the characters:
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

Examples:
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Input: s = "([)]"
Output: False

Technique: Stack

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "((()))",
        "({[]})"
    ]

    for test in test_cases:
        print(f"{test:<10} -> {solution.isValid(test)}")
