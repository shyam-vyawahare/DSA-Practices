"""
Task Scheduler

Given a list of tasks and a cooldown period n,
return the minimum number of time units required
to execute all tasks.

The same task must have at least n units between
two executions.

Greedy Strategy:
    Schedule the most frequent tasks first and use
    the remaining tasks to fill the available gaps.

Time Complexity:
    O(t), where t is the number of tasks.

Space Complexity:
    O(1), because there are at most 26 uppercase
    English letters.
"""


from collections import Counter


def least_interval(tasks, n):
    """
    Return the minimum number of time units required
    to complete all tasks.

    Args:
        tasks: List of task characters.
        n: Cooldown period.

    Returns:
        Minimum execution time.
    """

    if not tasks:
        return 0

    # Count how many times each task appears.
    frequencies = Counter(tasks)

    # Highest task frequency.
    max_freq = max(frequencies.values())

    # Number of tasks having the highest frequency.
    max_count = sum(
        1
        for frequency in frequencies.values()
        if frequency == max_freq
    )

    # Minimum schedule length required by the
    # most frequent tasks.
    required_time = (
        (max_freq - 1) * (n + 1)
        + max_count
    )

    # If there are enough other tasks to fill all
    # cooldown gaps, no idle time is necessary.
    return max(len(tasks), required_time)


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    result = least_interval(tasks, n)

    print("Minimum execution time:", result)
