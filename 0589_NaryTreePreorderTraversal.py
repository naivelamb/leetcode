"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

DFS

Time complexity: O(N)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = [root.val]
        for node in root.children:
            ans += self.preorder(node)

        return ans