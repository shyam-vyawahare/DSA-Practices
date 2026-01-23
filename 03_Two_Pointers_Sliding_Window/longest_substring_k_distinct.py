"""
Problem: Longest Substring with At Most K Distinct Characters
Technique: Sliding Window + Hash Map
Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        left = 0
        freq = {}
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
