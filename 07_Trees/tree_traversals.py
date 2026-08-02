"""
Topic: Binary Tree Traversals

A Binary Tree can be traversed in three Depth-First Search (DFS) orders:

1. Preorder  : Root -> Left -> Right
2. Inorder   : Left -> Root -> Right
3. Postorder : Left -> Right -> Root

Time Complexity:
- O(n) for all traversals

Space Complexity:
- O(h)
where h is the height of the tree.
Worst Case: O(n)
Balanced Tree: O(log n)
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Traversal:

    def preorder(self, root):
        """Root -> Left -> Right"""
        if root is None:
            return

        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        """Left -> Root -> Right"""
        if root is None:
            return

        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        """Left -> Right -> Root"""
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")


if __name__ == "__main__":

    """
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
    """

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    traversal = Traversal()

    print("Preorder : ", end="")
    traversal.preorder(root)

    print("\nInorder  : ", end="")
    traversal.inorder(root)

    print("\nPostorder: ", end="")
    traversal.postorder(root)
