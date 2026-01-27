"""
Problem: Remove Nth Node From End of List
Technique: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
