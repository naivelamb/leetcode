"""
https://leetcode.com/problems/number-of-1-bits/
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        binary = '{0:032b}'.format(n)
        for ch in binary:
            if ch == '1':
                ans += 1
        return ans