"""
https://leetcode.com/problems/reorder-list/

Find the mid point node, cut it, reverse the 2nd half.
Then two pointer.

Time complexity: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # find mid point
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # cut
        mid = slow.next
        slow.next = None
        # reverse 2nd half
        prev, curr = None, mid
        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        # two-pointer to rebuild the linked-list
        head1, head2 = head, prev
        while head2:
            head1_next, head2_next = head1.next, head2.next
            head1.next = head2
            head2.next = head1_next
            head1, head2 = head1_next, head2_next
