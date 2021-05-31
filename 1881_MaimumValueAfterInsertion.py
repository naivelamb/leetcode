"""
https://leetcode.com/problems/maximum-value-after-insertion/

For positive, find the first i such that n[i] < x, insert before it. 
For negative ,find the first i such that n[i] > x, insert before it. 

Time complexity: O(N), N = len(n)
"""
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != '-':
            for i, v in enumerate(n):
                if int(v) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i, v in enumerate(n):
                if i == 0:
                    pass
                elif int(v) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
                    