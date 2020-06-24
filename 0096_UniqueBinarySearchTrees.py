"""
https://leetcode.com/problems/unique-binary-search-trees/

DP[i] = number of unique BST for n
F[i, n] = number of unique BST for n using i as root.
DP[i] = sum(F[i, n]) for i in range(1, n+1)
For BST using i as root, there are (i-1) nodes in the left, (n-i) nodes in the right.
F[i, n] =  DP[i] * DP[n-i]

Time Complexity:O(N^2)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
