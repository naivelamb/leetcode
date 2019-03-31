# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/next-greater-node-in-linked-list/

Conver to list, then use stack to solve the problem.

Time complexity: O(n)
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
            
        res, stack = [], []
        
        for x in vals[::-1]:
            while stack and stack[-1] <= x:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1])
            stack.append(x)
        return res[::-1]

