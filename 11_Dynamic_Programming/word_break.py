"""
Word Break

Problem:
Given a string s and a dictionary of words, determine whether
s can be segmented into one or more dictionary words.

Example:
s = "leetcode"
word_dict = ["leet", "code"]

Output:
True
"""


def word_break(s, word_dict):
    """
    Determine whether s can be segmented into dictionary words
    using bottom-up dynamic programming.
    """

    n = len(s)

    # dp[i] = True if s[:i] can be formed using dictionary words
    dp = [False] * (n + 1)

    # Empty string can always be formed
    dp[0] = True

    word_set = set(word_dict)

    for i in range(1, n + 1):

        for j in range(i):
            # Check whether:
            # 1. s[:j] can already be formed
            # 2. s[j:i] is a dictionary word

            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# Example 1
s = "leetcode"
word_dict = ["leet", "code"]

print("String:", s)
print("Dictionary:", word_dict)
print("Can be segmented:", word_break(s, word_dict))


# Example 2
s = "catsandog"
word_dict = ["cats", "dog", "sand", "and", "cat"]

print("\nString:", s)
print("Dictionary:", word_dict)
print("Can be segmented:", word_break(s, word_dict))
