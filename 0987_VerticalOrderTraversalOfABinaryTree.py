# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

BFS. Remember the index of each node (root -> 0). If go left, index -= 1; if go
right, index += 1. 
Same level, same index, sort first then add to the recording dictionary.
Time complexity: O(n), n = number of nodes
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
import collections
class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        ref = collections.defaultdict(list)
        # (node, index) in the queue
        queue = [[root, 0]]
        # avoid sort index
        min_idx, max_idx = 0, 0
        while queue:
            tmp = []
            ref_tmp = collections.defaultdict(list)
            for node, idx in queue:
                min_idx = min(idx, min_idx)
                max_idx = max(idx, max_idx)
                ref_tmp[idx].append(node.val)
                if node.left:
                    tmp.append([node.left, idx - 1])
                if node.right:
                    tmp.append([node.right, idx + 1])
            queue = tmp
            # sort nodes in the same level
            for key in ref_tmp:
                ref[key] += sorted(ref_tmp[key])
        ans = []
        for key in range(min_idx, max_idx + 1):
            ans.append(ref[key])
        return ans
