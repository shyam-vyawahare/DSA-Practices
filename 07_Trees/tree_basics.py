"""
Topic: Binary Tree Basics

A Binary Tree is a hierarchical data structure in which
each node has at most two children:
1. Left Child
2. Right Child

Terminology:
- Root
- Parent
- Child
- Leaf
- Height
- Depth

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insertion: O(n)
- Deletion: O(n)

Space Complexity:
- O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    """Root -> Left -> Right"""
    if root is None:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":
    """
            1
          /   \
         2     3
        / \   /
       4   5 6
    """

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)

    print("Preorder Traversal:")
    preorder(root)
