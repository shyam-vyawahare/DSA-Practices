"""
Decode Ways

Problem:
A message containing letters A-Z can be encoded as:
A -> 1
B -> 2
...
Z -> 26

Given a string containing digits, return the number of ways
it can be decoded.

Example:
s = "226"

Possible decodings:
2 2 6  -> B B F
22 6   -> V F
2 26   -> B Z

Output:
3
"""


def num_decodings(s):
    """
    Return the number of possible decodings of s
    using dynamic programming.
    """

    if not s or s[0] == "0":
        return 0

    # prev2 = number of ways to decode up to i-2
    # prev1 = number of ways to decode up to i-1
    prev2 = 1
    prev1 = 1

    for i in range(1, len(s)):

        current = 0

        # Option 1:
        # Decode the current digit by itself.
        if s[i] != "0":
            current += prev1

        # Option 2:
        # Decode the current digit together with
        # the previous digit.
        two_digit = int(s[i - 1:i + 1])

        if 10 <= two_digit <= 26:
            current += prev2

        # Move forward
        prev2 = prev1
        prev1 = current

    return prev1


# Example 1
s = "226"

print("String:", s)
print("Number of decodings:", num_decodings(s))


# Example 2
s = "12"

print("\nString:", s)
print("Number of decodings:", num_decodings(s))


# Example 3
s = "06"

print("\nString:", s)
print("Number of decodings:", num_decodings(s))
