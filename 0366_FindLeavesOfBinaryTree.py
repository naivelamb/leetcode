"""
https://leetcode.com/problems/find-leaves-of-binary-tree/

DFS returns "level" 
leaf => 1
parent of leaf => 2
etc
And store the value in a dictionary. 

Then just traverse the dictionary. 

Time complexity: O(N)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Collection


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, dic):
            if not root:
                return 0
            left = dfs(root.left, dic)
            right = dfs(root.right, dic)
            level = max(left, right) + 1
            dic[level].append(root.val)
            return level

        dic, ans = collections.defaultdict(list), []
        dfs(root, dic)
        for i in range(1, len(dic) + 1):
            ans.append(dic[i])
        return ans