"""
Problem: Daily Temperatures

Given an array of integers temperatures representing the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature.

If there is no future day for which this is possible, keep answer[i] == 0.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Technique: Monotonic Stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # Stores indices

        for current_day, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                previous_day = stack.pop()
                result[previous_day] = current_day - previous_day

            stack.append(current_day)

        return result


if __name__ == "__main__":
    solution = Solution()

    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    print("Temperatures :", temperatures)
    print("Days to Wait :", solution.dailyTemperatures(temperatures))
