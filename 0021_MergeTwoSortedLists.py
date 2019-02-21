# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/merge-two-sorted-lists/

Two pointers, scan, O(m + n)
"""
class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val > l2.val:
            head = l2
            l2.next = self.mergeTwoLists(l1, l2.next)
        else:
            head = l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return head