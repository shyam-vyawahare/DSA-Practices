"""
Problem: Linked List Cycle
Technique: Fast & Slow Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
