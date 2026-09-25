"""
Partition Equal Subset Sum

Problem:
Given an array of positive integers, determine whether the array
can be partitioned into two subsets with equal sums.

Example:
nums = [1, 5, 11, 5]

Output:
True
"""


def can_partition(nums):
    """
    Determine whether nums can be divided into two subsets
    having equal sums.

    Uses 0/1 Knapsack-style dynamic programming.
    """

    total = sum(nums)

    # An odd total cannot be divided into two equal integers.
    if total % 2 != 0:
        return False

    target = total // 2

    # dp[s] = True if sum s can be created using
    # the numbers processed so far.
    dp = [False] * (target + 1)

    # Sum 0 is always possible by choosing nothing.
    dp[0] = True

    for num in nums:

        # Traverse backwards so each number is used at most once.
        for current_sum in range(target, num - 1, -1):

            dp[current_sum] = (
                dp[current_sum]
                or dp[current_sum - num]
            )

    return dp[target]


# Example 1
nums = [1, 5, 11, 5]

print("Array:", nums)
print("Can be partitioned:", can_partition(nums))


# Example 2
nums = [1, 2, 3, 5]

print("\nArray:", nums)
print("Can be partitioned:", can_partition(nums))
