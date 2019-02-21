# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reverse-linked-list/

@author: Xuan-Laptop
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head