"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Standard BFS.

Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        curr = [root]
        while curr:
            tmp, val = [], 0
            for node in curr:
                val += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ans.append(val/len(curr))
            curr = tmp
        return ans