"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Do it recursively.
At each non-empty node, we need to do following,
1. Check if node has children, if so, link left & right.
2. Check if node has next, if so, link node.right and node.next.left.
3. Do #1 and #2 for left and right children.

Time complexity: O(N)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node and node.left:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return root