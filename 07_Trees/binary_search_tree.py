"""
Topic: Binary Search Tree (BST)

Properties:
1. Left subtree values < Root
2. Right subtree values > Root

Average Complexity:
Search : O(log n)
Insert : O(log n)

Worst Case:
O(n)
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)


if __name__ == "__main__":

    bst = BinarySearchTree()

    root = None

    for value in [50, 30, 70, 20, 40, 60, 80]:
        root = bst.insert(root, value)

    print("Inorder Traversal:")
    bst.inorder(root)

    print("\nSearching 60...")

    if bst.search(root, 60):
        print("Found")
    else:
        print("Not Found")
