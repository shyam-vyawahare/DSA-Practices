"""
Jump Game

Given an array where nums[i] represents the maximum
jump length from index i, determine whether the last
index can be reached.

Greedy Strategy:
    Track the farthest index that can be reached so far.

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def can_jump(nums):
    """
    Return True if the last index is reachable,
    otherwise return False.

    Args:
        nums: List of maximum jump lengths.

    Returns:
        True if the last index can be reached.
        False otherwise.
    """

    farthest = 0

    for i in range(len(nums)):

        # If the current index is beyond our reachable
        # range, we can never get to the last index.
        if i > farthest:
            return False

        # Update the farthest position we can reach.
        farthest = max(farthest, i + nums[i])

        # If the last index is already reachable,
        # we can stop early.
        if farthest >= len(nums) - 1:
            return True

    return True


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]

    result = can_jump(nums)

    print("Can reach last index:", result)
