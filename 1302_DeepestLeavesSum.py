"""
https://leetcode.com/problems/deepest-leaves-sum/

BFS.
Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ref = collections.defaultdict(list)
        curr_level = 0
        nodes = [root]
        while nodes:
            tmp = []
            for node in nodes:
                ref[curr_level].append(node.val)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            curr_level += 1
            nodes = tmp
        return sum(ref[curr_level - 1])