"""
Problem: Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes.

The lowest common ancestor is the lowest node in the tree
that has both p and q as descendants.

A node can be a descendant of itself.

Example:

        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

p = 5
q = 1

Output: 3

Technique: DFS + Recursion

Time Complexity: O(n)
Space Complexity: O(h)

where h is the height of the tree.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode
    ) -> Optional[TreeNode]:

        # If root is None or root is one of the target nodes,
        # return root.
        if root is None or root == p or root == q:
            return root

        # Search in the left subtree.
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search in the right subtree.
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides found a target node,
        # current root is the LCA.
        if left and right:
            return root

        # Otherwise return whichever side contains a target.
        return left if left else right


if __name__ == "__main__":

    """
            3
           / \
          5   1
         / \ / \
        6  2 0  8
          / \
         7   4
    """

    root = TreeNode(3)

    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left
    q = root.right

    solution = Solution()

    ancestor = solution.lowestCommonAncestor(root, p, q)

    print("Lowest Common Ancestor:", ancestor.val)
