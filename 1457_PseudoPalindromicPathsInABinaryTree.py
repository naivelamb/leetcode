"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

Record the cnt of values from root to leaf. A path is pseudoPalindromicPath if,
1). Node count is even and all counts are even.
or
2). Node count is odd and only one count is odd. 
Time compleixty: O(N), N = # of nodes
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans
        cnt = [0] * 9
        cnt[root.val - 1] = 1
        stack = [(root, cnt)]
        while stack:
            node, cnt = stack.pop()
            if not node.left and not node.right:
                # leaf
                n, n_odd = sum(cnt), 0
                for x in cnt:
                    n_odd = n_odd + (x % 2)
                if n % 2 == 0 and n_odd == 0:
                    ans += 1
                if n % 2 == 1 and n_odd == 1:
                    ans += 1
            else:
                if node.left:
                    cnt_tmp = cnt.copy()
                    cnt_tmp[node.left.val - 1] += 1
                    stack.append((node.left, cnt_tmp))
                if node.right:
                    cnt_tmp = cnt.copy()
                    cnt_tmp[node.right.val - 1] += 1
                    stack.append((node.right, cnt_tmp))
        return ans