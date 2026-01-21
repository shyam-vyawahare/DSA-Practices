"""
Concept: Prefix Sum
Use Case: Range Sum Queries
Preprocessing: O(n)
Query Time: O(1)
"""

class PrefixSum:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def range_sum(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
