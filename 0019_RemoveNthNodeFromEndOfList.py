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
        p2, i = head, n
        while i != 0 and p2:
            p2 = p2.next
            i -= 1
        
        dummy = ListNode()
        dummy.next = head
        prev, p1 = dummy, head
        while p2:
            p1 = p1.next
            p2 = p2.next
            prev = prev.next
        
        if p2:
            prev.next = p1.next
        else:
            prev.next = None

        return dummy.next