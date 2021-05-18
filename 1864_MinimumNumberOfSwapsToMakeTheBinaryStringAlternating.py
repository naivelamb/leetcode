"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

Track number of '0' on odd position (n01) and even position (n00). 

If abs(n - 2 * n00 - 2 * n01) > 1, no way to alternating, return -1

If n % 2 == 1,
n00 + n01 > n // 2, 0 is more than 1, 0 must be on even position, return n01
else return n00

Else, return min(n00, n01)


Time complexity: O(N)
"""
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        n00, n01 = 0, 0
        for i, x in enumerate(s):
            if x == '0':
                if i % 2 == 0:
                    n00 += 1
                else:
                    n01 += 1
        n0 = n00 + n01
        if abs(n - n0*2) > 1:
            return -1
        
        if n % 2 == 1:
            if n00 + n01 > n // 2: # 0 must be even
                return n01
            else: # 0 must be odd 
                return n00
        else:
            return min(n01, n00)        
        
