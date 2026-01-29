"""
Problem: Valid Parentheses

Given a string s containing just the characters:
'(', ')', '{', '}', '[', ']',
determine if the input string is valid.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket.

Example:
Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Technique: Stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
