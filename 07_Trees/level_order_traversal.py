"""
Problem: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order
traversal of its nodes' values.

(Level by level, from left to right.)

Example:

        3
      /   \
     9     20
          /  \
         15   7

Output:
[[3], [9, 20], [15, 7]]

Technique: Breadth-First Search (BFS)

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result


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

    print("Level Order Traversal:")
    print(solution.levelOrder(root))
