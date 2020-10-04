"""
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
Observation 1:
1 -> 0 needs 1 operation,
2 -> 0 needs 3 operation,
4 -> 0 needs 7 operations.
2^k -> 0 needs (2^(k+1) - 1) operations.

Observation 2:
if a -> b takes k operations, then b -> a also takes k operations.

For something like XXXXXXXX1, we need to do the transform
XXXXXXXX1 -> 000000011 -> 000000001 -> 000000000

Time complexity: O(logN)
"""
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        bina = bin(n)[2:]
        n = len(bina)
        sign = 1
        ans = 0
        for i in range(n):
            digit = int(bina[i])
            if not digit:
                continue
            ans += ((2**(n-(i+1)))*2 - 1) * sign
            sign *= -1
        return ans

    def minimumOneBitOperations_dp(self, n: int) -> int:
        dp = {0: 0}
        def helper(n):
            if n not in dp:
                b = 1
                while (b << 1) < n:
                    b = b << 1
                dp[n] = helper((b >> 1) ^ b ^ n) + 1 + b - 1
            return dp[n]
        return helper(n)
