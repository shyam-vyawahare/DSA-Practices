"""
Activity Selection Problem

Given a set of activities with start and finish times,
select the maximum number of non-overlapping activities.

Greedy Strategy:
    Always choose the activity that finishes earliest.

Time Complexity:
    O(n log n) - sorting
    O(n)       - selecting activities

Space Complexity:
    O(n) - sorted activities
"""


def activity_selection(activities):
    """
    Select the maximum number of non-overlapping activities.

    Each activity is represented as:
        (start_time, finish_time)

    Example:
        activities = [
            (1, 3),
            (2, 4),
            (3, 5),
            (0, 6),
            (5, 7),
            (8, 9),
            (5, 9)
        ]

    Returns:
        List of selected activities.
    """

    # Sort activities by their finish time.
    activities.sort(key=lambda activity: activity[1])

    selected = []

    # No activity has been selected yet.
    last_finish = float("-inf")

    for start, finish in activities:

        # Select the activity if it does not overlap
        # with the previously selected activity.
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


if __name__ == "__main__":
    activities = [
        (1, 3),
        (2, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (8, 9),
        (5, 9)
    ]

    result = activity_selection(activities)

    print("Selected activities:", result)
    print("Maximum activities:", len(result))
