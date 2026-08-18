"""
Problem: Merge K Sorted Lists

You are given an array of k linked lists, where each linked
list is sorted in ascending order.

Merge all the linked lists into one sorted linked list
and return its head.

Example:

Input:
[
    1 -> 4 -> 5,
    1 -> 3 -> 4,
    2 -> 6
]

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Technique:
Min Heap + Linked Lists

Time Complexity:
O(N log k)

Where:
N = total number of nodes
k = number of linked lists

Space Complexity:
O(k)
"""


import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        min_heap = []

        # Add the first node of every non-empty list.
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(
                    min_heap,
                    (node.val, index, node)
                )

        dummy = ListNode(0)
        current = dummy

        while min_heap:

            value, index, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            # Add the next node from the same list.
            if node.next:
                heapq.heappush(
                    min_heap,
                    (node.next.val, index, node.next)
                )

        return dummy.next


def create_linked_list(values):
    """Create a linked list from a Python list."""

    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    """Print linked list values."""

    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(" -> ".join(map(str, values)))


if __name__ == "__main__":

    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]

    solution = Solution()

    merged = solution.mergeKLists(lists)

    print("Merged Linked List:")
    print_linked_list(merged)
