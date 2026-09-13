"""
Jump Game II

Given an array where nums[i] represents the maximum
jump length from index i, return the minimum number
of jumps required to reach the last index.

The last index is guaranteed to be reachable.

Greedy Strategy:
    Treat all positions reachable with the current
    number of jumps as a range and find the farthest
    position reachable from that range.

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def jump(nums):
    """
    Return the minimum number of jumps required
    to reach the last index.

    Args:
        nums: List of maximum jump lengths.

    Returns:
        Minimum number of jumps.
    """

    jumps = 0
    current_end = 0
    farthest = 0

    # We don't need to process the last index because
    # reaching it means the problem is already solved.
    for i in range(len(nums) - 1):

        # Find the farthest position reachable
        # from the current jump range.
        farthest = max(farthest, i + nums[i])

        # We have reached the end of the current range.
        # We must make another jump.
        if i == current_end:
            jumps += 1
            current_end = farthest

            # The last index is now reachable.
            if current_end >= len(nums) - 1:
                break

    return jumps


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]

    result = jump(nums)

    print("Minimum jumps:", result)
