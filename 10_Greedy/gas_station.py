"""
Gas Station

Given two circular arrays:
    gas[i]  = gas available at station i
    cost[i] = gas required to travel from station i
              to the next station

Return the starting station index from which we can
complete the entire circular route.

If no valid starting station exists, return -1.

Greedy Strategy:
    Track the current tank balance.
    If the balance becomes negative at station i,
    the current start and every station before i
    cannot be a valid starting point.

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def can_complete_circuit(gas, cost):
    """
    Return the valid starting station index.

    Args:
        gas: List of gas available at each station.
        cost: List of travel costs to the next station.

    Returns:
        Starting station index, or -1 if impossible.
    """

    # If the total available gas is less than the
    # total required gas, completing the circuit
    # is impossible regardless of the starting point.
    if sum(gas) < sum(cost):
        return -1

    start = 0
    tank = 0

    for i in range(len(gas)):

        # Net gas gained/lost at this station.
        tank += gas[i] - cost[i]

        # We cannot reach the next station from
        # the current starting point.
        if tank < 0:
            # The current start and every station
            # between start and i are invalid.
            start = i + 1
            tank = 0

    return start


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    result = can_complete_circuit(gas, cost)

    print("Starting station:", result)
