# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

BFS. Assign each node with an index. Check whether the index of the last node
equals to the # of nodes.

Time Complexity: O(n), n => number of nodes
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: 'TreeNode') -> 'bool':
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((nodes.left, 2*v))
                nodes.append((nodes.right, 2*v+1))
        return nodes[-1][1] == len(nodes)
                