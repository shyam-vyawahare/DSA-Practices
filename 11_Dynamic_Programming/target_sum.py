"""
Target Sum

Problem:
Given an array of integers, assign either '+' or '-' to each
number so that the resulting expression equals target.

Return the number of different ways.

Example:
nums = [1, 1, 1, 1, 1]
target = 3

Output:
5
"""


def find_target_sum_ways(nums, target):
    """
    Count the number of ways to assign '+' and '-' signs
    so that the expression equals target.

    Uses a subset-sum transformation with 0/1 Knapsack DP.
    """

    total = sum(nums)

    # If the target is outside the possible range,
    # no solution exists.
    if abs(target) > total:
        return 0

    # Derivation:
    #
    # Positive subset = P
    # Negative subset = N
    #
    # P + N = total
    # P - N = target
    #
    # Therefore:
    #
    # P = (total + target) / 2

    if (total + target) % 2 != 0:
        return 0

    subset_sum = (total + target) // 2

    # dp[s] = number of ways to create sum s
    dp = [0] * (subset_sum + 1)

    # There is one way to create sum 0:
    # choose nothing.
    dp[0] = 1

    for num in nums:

        # Traverse backwards because each number
        # can be used only once.
        for current_sum in range(subset_sum, num - 1, -1):

            dp[current_sum] += dp[current_sum - num]

    return dp[subset_sum]


# Example 1
nums = [1, 1, 1, 1, 1]
target = 3

print("Array:", nums)
print("Target:", target)
print("Number of ways:", find_target_sum_ways(nums, target))


# Example 2
nums = [1, 2, 3, 4]
target = 0

print("\nArray:", nums)
print("Target:", target)
print("Number of ways:", find_target_sum_ways(nums, target))
