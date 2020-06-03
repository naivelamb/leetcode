"""
https://leetcode.com/problems/counting-bits/
DP
The results of [2**k, 2**(k+1) - 1] is a replication of [0, 2**(k-1)], add 1 to every element.

"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        i, base = 0, 1
        while i + base <= num:
            while i <= base and i + base <= num:
                dp[i+base] = 1 + dp[i]
                i += 1
            i = 0
            base *= 2
        return dp
