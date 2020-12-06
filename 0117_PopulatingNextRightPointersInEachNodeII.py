"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

BFS, layer by layer, space O(N)
BFS node based, record previous, compare level, space O(1)
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
        if not root:
            return root
        queue = collections.deque([])
        queue.append([root, 0])
        prev_node, prev_level = None, -1
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
            if prev_node and prev_level == level:
                prev_node.next = node
            prev_node, prev_level = node, level
        return root        