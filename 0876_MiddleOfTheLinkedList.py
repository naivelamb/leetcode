"""
https://leetcode.com/problems/middle-of-the-linked-list/

#1 Loop twice. O(2N)
#2 Two-pointer, p1 jumps 1 step a time, p2 jumps 2 step a time. O(N)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
        return p1
