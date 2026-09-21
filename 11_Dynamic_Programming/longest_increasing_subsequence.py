"""
Longest Increasing Subsequence

Given an integer array, find the length of the longest
strictly increasing subsequence.

A subsequence does not need to contain consecutive elements.

DP Pattern:
    Subsequence DP

State:
    dp[i] = length of the longest increasing subsequence
            ending at index i

Transition:
    If nums[j] < nums[i]:

        dp[i] = max(dp[i], dp[j] + 1)

Time Complexity:
    O(n^2)

Space Complexity:
    O(n)
"""


def length_of_lis(nums):
    """
    Return the length of the longest increasing subsequence.

    Args:
        nums: List of integers.

    Returns:
        Length of the longest increasing subsequence.
    """

    if not nums:
        return 0

    # Every element can form an increasing subsequence
    # of length 1 by itself.
    dp = [1] * len(nums)

    for i in range(len(nums)):

        # Check every element before nums[i].
        for j in range(i):

            # nums[i] can extend the increasing
            # subsequence ending at nums[j].
            if nums[j] < nums[i]:

                dp[i] = max(
                    dp[i],
                    dp[j] + 1
                )

    return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    result = length_of_lis(nums)

    print("Length of LIS:", result)
