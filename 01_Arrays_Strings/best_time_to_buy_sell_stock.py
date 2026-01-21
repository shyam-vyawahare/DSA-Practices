"""
Problem: Best Time to Buy and Sell Stock
Technique: Single Pass (Greedy)
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
