"""
https://leetcode.com/problems/count-vowels-permutation/

a->0
e->1
i->2
o->3
u->4

dp[i][j] => number of permutation of length-i ending with vowel-j

possible sequence:
ae -> 01
ea -> 10
ei -> 12
ia -> 20
ie -> 21
io -> 23
iu -> 24
oi -> 32
ou -> 34
ua -> 40

dp[i][0] = sum(dp[i-1][j] for j in [1, 2, 4]]
dp[i][1] = sum(dp[i-1][j] for j in [0, 2]]
dp[i][2] = sum(dp[i-1][j] for j in [1, 3]]
dp[i][3] = sum(dp[i-1][j] for j in [2]]
dp[i][3] = sum(dp[i-1][j] for j in [2, 3]]

Time complexity: O(5N)
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 5 for _ in range(n + 1)]
        for j in range(5):
            dp[1][j] = 1
        
        cands = [[1,2,4], [0,2], [1,3], [2], [2,3]]
        for i in range(2, n + 1):
            for j in range(5):
                dp[i][j] = sum(dp[i-1][k] for k in cands[j])
        return sum(dp[-1]) % MOD