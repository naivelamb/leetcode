# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/

BFS, get all the strings from leaf to root, and compare them every time we get a new string. 
Time complexity: O(n), n = number of nodes
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
import collections
class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        
        def get_char(n):
            # return char given the integer
            return chr(ord('a') + n)
        
        # bfs
        queue = collections.deque()
        queue.append([root, 1, get_char(root.val)])
        ans = ''
        while queue:
            node, level, curr = queue.popleft()
            if not node.left and not node.right:
                # find leaf
                if not ans:
                    ans = curr
                else:
                    ans = sorted([ans, curr])[0]
            if node.left:
                new_chr = get_char(node.left.val) + curr
                queue.append([node.left, level + 1, new_chr])
            if node.right:
                new_chr = get_char(node.right.val) + curr
                queue.append([node.right, level + 1, new_chr])      
        return ans