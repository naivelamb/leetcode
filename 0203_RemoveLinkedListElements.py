"""
https://leetcode.com/problems/remove-linked-list-elements/

If curr.val == val, prev.next = curr.next.

Time complexity: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next

        return dummy.next
