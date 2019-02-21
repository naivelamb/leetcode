# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/add-two-numbers/

add by digit, carry
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        carry = 0
        dummy = curr = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        
        return dummy.next