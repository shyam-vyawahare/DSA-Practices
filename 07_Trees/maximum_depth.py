"""
Problem: Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

Example:

        3
      /   \
     9     20
          /  \
         15   7

Output:
3

Technique: Depth-First Search (DFS) + Recursion

Time Complexity: O(n)
Space Complexity: O(h)

where h is the height of the tree.
Worst Case: O(n)
Balanced Tree: O(log n)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


if __name__ == "__main__":

    """
            3
          /   \
         9     20
              /  \
             15   7
    """

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    print("Maximum Depth:", solution.maxDepth(root))
