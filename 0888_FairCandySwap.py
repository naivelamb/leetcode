"""
https://leetcode.com/problems/fair-candy-swap/

A = sum(A), B = sum(B)
If A removes x, we are looking for y, such that
A - x + y = B - y + x
==> A + 2y = B + 2x

Tranfer both to set, for all x in A, find if y exists in B.

Time complexity: O(M + N)
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s1, s2 = sum(A), sum(B)
        A, B = set(A), set(B)
        
        for x in A:
            y = int((s2 - s1 + 2 * x)/2)
            if y in B:
                return [x, y]