# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/

For a given node, count the balance needed to make it balance. 
Positive means it will give coins back to the parent.
Negative means it need coin from the parent.

Then for a node, 
balance = node.val + left.balance + right.balance - 1
moves += abs(left.balance) + abs(right.balance)
"""
class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + R + L - 1
        dfs(root)
        return self.ans
