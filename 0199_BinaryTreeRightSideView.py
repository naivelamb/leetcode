"""
https://leetcode.com/problems/binary-tree-right-side-view/

BFS
Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        ans, curr = [], [root]
        while curr:
            ans.append(curr[-1].val)
            tmp = []
            for node in curr:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            curr = tmp
        return ans