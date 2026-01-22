"""
Problem: Valid Anagram
Technique: Frequency Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1

        return True
