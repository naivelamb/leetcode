"""
https://leetcode.com/problems/number-complement/
"""
class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        ans = 0
        for i, ch in enumerate(num[::-1]):
            ans += (1 - int(ch)) * 2**i
        return ans

sol = Solution()
assert sol.findComplement(5) == 2
assert sol.findComplement(1) == 0
