"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Move a pointer n steps first, then create another pointer from head, move two pointers together untill the first point hit end, now we find the node we need to delet. 

Time complexity: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        last = head
        i = n
        while i != 0 and last:
            last = last.next
            i -= 1

        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head
        while last:
            prev = prev.next
            curr = curr.next
            last = last.next

        if curr:
            prev.next = curr.next
        else:
            prev.next = None
        return dummy.next