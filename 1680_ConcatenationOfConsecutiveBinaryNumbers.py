"""
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

Recursion. 
k = len(bin(n)) - 2
f(n) = f(n-1) * 2**k + n

Time complexity: O(N)
"""

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return 1
        k = len(bin(n)) - 2
        return (self.concatenatedBinary(n - 1) * 2**k + n) % (10**9 + 7)