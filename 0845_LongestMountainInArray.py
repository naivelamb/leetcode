"""
https://leetcode.com/problems/longest-mountain-in-array/

Go through the array, count up and down. 
We reset up and down when we see:
1. non-zero down and A[i] > A[i-1]
2. A[i] == A[i-1]

Find the longest mountain. 

Time complexity: O(N)
"""
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i] > A[i-1] or A[i] == A[i-1]:
                up = down = 0
            
            up += A[i] > A[i-1]
            down += A[i] < A[i-1]

            if up and down:
                res = max(res, up + down + 1)
        return res