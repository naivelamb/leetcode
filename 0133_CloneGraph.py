"""
https://leetcode.com/problems/clone-graph/

dfs the original graph, hash the original node and new node, connect the neighbors.

Time complexity: O(V), V = # of nodes.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        root = Node(node.val)
        ref = {}
        ref[node] = root
        stack = [node]
        while stack:
            curr = stack.pop()
            for nei in curr.neighbors:
                if nei not in ref:
                    stack.append(nei)
                    ref[nei] = Node(nei.val)
                ref[curr].neighbors.append(ref[nei])
        return root