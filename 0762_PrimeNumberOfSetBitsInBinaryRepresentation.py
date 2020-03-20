"""
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
"""
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for x in range(L, R+1):
            if bin(x).count('1') in primes:
                ans += 1
        return ans
