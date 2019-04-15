# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:33:34 2019

#1 iterative
We can easily paser the string to get the value and its depth. We need to put 
the new node as the child of the lase seen node wieth depth = curr_depth - 1. 

Time complexity: O(n), n = len(S)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def recoverFromPreorder(self, S):
        ref = {}
        d, tmp = 0, ''
        for i, ch in enumerate(S):
            if ch != '-':
                tmp += ch
            else:
                if tmp:
                    node = TreeNode(int(tmp))
                    ref[d] = node
                    if d == 0:
                        root = node
                    else:
                        if ref[d-1].left:
                            ref[d-1].right = node
                        else:
                            ref[d-1].left = node
                    tmp = ''
                    d = 1
                else:
                    d += 1
        node = TreeNode(int(tmp))
        if d == 0:
            return node
        else:
            if ref[d-1].left:
                ref[d-1].right = node
            else:
                ref[d-1].left = node
        return root