# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

Use stack to remember the nodes we have seen. If see two '#' consecutively, we 
need to make sure before the two '#' we have a value, we need to pop these three
and append a '#', indicating this subtree is valid. 

Time complexity: O(n)
"""
class Solution:
    def isValidSerialization(self, preorder):
        stack = []
        for s in preorder.split(','):
            if s == '#':
                while len(stack) >= 2 and stack[-1] == '#' and stack[-2] != '#':
                    stack.pop()
                    stack.pop()
            stack.append(s)
        return stack == ['#']