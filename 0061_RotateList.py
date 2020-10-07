"""
https://leetcode.com/problems/rotate-list/

1. Get the length of the list, find the tail.
2. Connect tail with head.
3. Get the move we need to make (k % n)
4. Use two pointers to check curr and prev node, move along  the list, cut the connection and return new head.

Time complexity: O(N) 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        tail.next = head
        k = k % n
        prev, curr = head, head.next

        while n > k + 1:
            prev = prev.next
            curr = curr.next
            n -= 1
        prev.next = None
        return curr
