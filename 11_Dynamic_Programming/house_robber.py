"""
House Robber

Given an array where nums[i] represents the amount of
money available in house i, determine the maximum amount
of money that can be robbed without robbing two adjacent
houses.

DP Pattern:
    Take or Skip

Recurrence:
    dp[i] = max(
        dp[i - 1],
        dp[i - 2] + nums[i]
    )

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def rob(nums):
    """
    Return the maximum amount of money that can be robbed.

    Args:
        nums: List of money available in each house.

    Returns:
        Maximum amount of money that can be robbed.
    """

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    # Maximum money from the first house.
    previous = nums[0]

    # Maximum money from the first two houses.
    current = max(nums[0], nums[1])

    for i in range(2, len(nums)):

        # Option 1: Skip the current house.
        skip = current

        # Option 2: Rob the current house.
        rob_current = previous + nums[i]

        # Choose the better option.
        next_value = max(skip, rob_current)

        previous = current
        current = next_value

    return current


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]

    result = rob(nums)

    print("Maximum money:", result)
