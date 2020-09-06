"""
https://leetcode.com/problems/image-overlap/
If two position overlap after shift, they have the same hamilton distance.

Time Complexity: O(N^4)
"""
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        LA = [i//n*100 + i%n for i in range(n**2) if A[i//n][i%n] == 1]
        LB = [i//n*100 + i%n for i in range(n**2) if B[i//n][i%n] == 1]
        c = collections.Counter(i-j for i in LA for j in LB)
        return max(c.values() or [0])
