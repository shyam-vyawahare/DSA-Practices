"""
Coin Change

Given a list of coin denominations and a target amount,
return the minimum number of coins required to make that
amount.

Each coin can be used unlimited times.

If the amount cannot be formed, return -1.

DP Pattern:
    Unbounded Knapsack
    Minimum DP

State:
    dp[i] = minimum number of coins required to make
            amount i

Transition:
    dp[i] = min(dp[i], dp[i - coin] + 1)

Time Complexity:
    O(amount * number_of_coins)

Space Complexity:
    O(amount)
"""


def coin_change(coins, amount):
    """
    Return the minimum number of coins required
    to make the given amount.

    Args:
        coins: List of available coin denominations.
        amount: Target amount.

    Returns:
        Minimum number of coins, or -1 if impossible.
    """

    # A value larger than the possible number of coins
    # is used as an initial "impossible" value.
    infinity = amount + 1

    dp = [infinity] * (amount + 1)

    # Zero coins are needed to make amount 0.
    dp[0] = 0

    for current_amount in range(1, amount + 1):

        for coin in coins:

            # We can use this coin only if it does not
            # exceed the current amount.
            if coin <= current_amount:

                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    # If dp[amount] was never updated, the amount
    # cannot be formed.
    if dp[amount] == infinity:
        return -1

    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11

    result = coin_change(coins, amount)

    print("Minimum coins:", result)
