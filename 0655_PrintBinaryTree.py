# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/print-binary-tree/

Clearly, if the tree's height is h, we have (2^h - 1) slots to fill. 
Next we need to find the location of each node. Take the following tree as an 
example:
          1
      2      3
        4
h = 3, we have n = 2^3 - 1 = 7 slots.
1 is the mid of (0, n-1)
2 is the mid of (0, location of 1 - 1)
3 is the mid of (location of 1 + 1, n-1)
4 is the mid of (location of 2, location of 1 - 1)

For a node, we need to know its 'left' and 'right' boundary, its location is 
mid = (left + right) // 2
For node.left, its boundary is 'left' and (mid - 1)
For node.right, its boundary is (mid + 1) and 'right'
=> recursion.

Time complexity: O(h(2^h - 1))
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root: TreeNode):
        def height(root):
            if not root:
                return 0
            return (1 + max(height(root.left),  height(root.right)))
        
        def construct(root, row, l, r):
            if not root:
                return
            mid = (l + r) // 2
            matrix[row][mid] = str(root.val)
            
            construct(root.left, row + 1, l, mid - 1)
            construct(root.right, row + 1, mid + 1, r)
            
        h = height(root)
        n = 2**h - 1
        matrix = [[''] * n for _ in range(h)]
        construct(root, 0, 0, n-1)
        return matrix
        
