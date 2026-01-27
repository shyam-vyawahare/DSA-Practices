"""
Problem: Middle of the Linked List
Technique: Fast & Slow Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def middleNode(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
