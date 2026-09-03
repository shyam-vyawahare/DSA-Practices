"""
Greedy Algorithms - Fundamentals

A greedy algorithm makes the best possible choice at each step
with the hope that these local choices lead to a globally optimal solution.

Key idea:
    Choose the option that looks best RIGHT NOW.

Greedy algorithms are useful when:
    1. A locally optimal choice can lead to a global optimum.
    2. Previous choices do not need to be reconsidered.
"""


def minimum_coins(amount, coins):
    """
    Find the minimum number of coins needed to make an amount.

    Assumes the coin denominations allow the greedy strategy
    to produce an optimal result.

    Example:
        amount = 41
        coins = [25, 10, 5, 1]

        25 + 10 + 5 + 1 = 41
        Number of coins = 4
    """

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count


def maximum_items(budget, prices):
    """
    Buy the maximum number of items within a given budget.

    Greedy strategy:
        Always buy the cheapest available item first.

    Example:
        budget = 10
        prices = [3, 1, 2, 5]

        Buy 1, 2, 3 -> 3 items
    """

    prices.sort()

    count = 0

    for price in prices:
        if budget < price:
            break

        budget -= price
        count += 1

    return count


def maximize_sum(numbers, k):
    """
    Maximize the sum by selecting the k largest numbers.

    Greedy strategy:
        Always select the largest available value.
    """

    numbers.sort(reverse=True)

    return sum(numbers[:k])


if __name__ == "__main__":
    # Example 1: Minimum coins
    coins = [25, 10, 5, 1]
    amount = 41

    print("Minimum coins:", minimum_coins(amount, coins))

    # Example 2: Maximum items within budget
    prices = [3, 1, 2, 5]
    budget = 10

    print("Maximum items:", maximum_items(budget, prices))

    # Example 3: Maximum sum
    numbers = [10, 3, 7, 8, 2]
    k = 3

    print("Maximum sum:", maximize_sum(numbers, k))
