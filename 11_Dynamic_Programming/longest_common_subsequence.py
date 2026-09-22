"""
Longest Common Subsequence (LCS)

Problem:
Given two strings, find the length of their longest common subsequence.

Example:
text1 = "abcde"
text2 = "ace"

LCS = "ace"
Answer = 3
"""


def longest_common_subsequence(text1, text2):
    """
    Find the length of the longest common subsequence
    using bottom-up dynamic programming.
    """

    m = len(text1)
    n = len(text2)

    # dp[i][j] = LCS length of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:
                # Matching characters extend the LCS
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                # Skip one character from either string
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


# Example
text1 = "abcde"
text2 = "ace"

result = longest_common_subsequence(text1, text2)

print("Text 1:", text1)
print("Text 2:", text2)
print("Longest Common Subsequence Length:", result)
