"""
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

Sort the two cuts, find the maximum difference between two consecutive cuts. Answer is the product.

Time complexity: O(nlogn + mlogm)
"""

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        A = sorted([0, h] + horizontalCuts)
        B = sorted([0, w] + verticalCuts)
        x = 0
        for i in range(1, len(A)):
            x = max(x, A[i] - A[i-1])
        y = 0
        for i in range(1, len(B)):
            y = max(y, B[i] - B[i-1])
        return x * y % MOD