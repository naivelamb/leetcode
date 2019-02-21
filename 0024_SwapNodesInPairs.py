# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/swap-nodes-in-pairs/

[1, 2, 3, 4] -> [2, 1, 4, 3]
[1, 2, 3, 4, 5] -> [2, 1, 4, 3, 5]

take 1st, 2nd and 3rd,

2nd -> 1st -> swap(3rd)

Time Complexity： O(n)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        first, second, third = head, head.next, head.next.next
        head = second
        head.next = first
        first.next = self.swapPairs(third)
        
        return head