"""
Non-overlapping Intervals

Given a collection of intervals, return the minimum number
of intervals that must be removed so that the remaining
intervals do not overlap.

Greedy Strategy:
    Sort intervals by their ending time.
    Always keep the interval that finishes earliest.

Time Complexity:
    O(n log n)

Space Complexity:
    O(1) auxiliary space
"""


def erase_overlap_intervals(intervals):
    """
    Return the minimum number of intervals to remove.

    Args:
        intervals: List of [start, end] intervals.

    Returns:
        Minimum number of intervals that must be removed.
    """

    if not intervals:
        return 0

    # Sort by ending time.
    intervals.sort(key=lambda interval: interval[1])

    removals = 0

    # End time of the last interval we decided to keep.
    last_end = intervals[0][1]

    for start, end in intervals[1:]:

        # Overlap detected.
        if start < last_end:
            removals += 1

        else:
            # No overlap, so keep this interval.
            last_end = end

    return removals


if __name__ == "__main__":
    intervals = [
        [1, 2],
        [2, 3],
        [3, 4],
        [1, 3]
    ]

    result = erase_overlap_intervals(intervals)

    print("Minimum intervals to remove:", result)
