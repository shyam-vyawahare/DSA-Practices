"""
Problem: Merge Two Sorted Lists
Technique: Pointer Traversal
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return dummy.next
