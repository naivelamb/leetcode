"""
https://leetcode.com/problems/arithmetic-slices/

If we have an arithmetic array of length k (k >= 3), then we can build 
(k-1)(k-2)/2 arithmetic slices. 

For a given start position i, We need to find the longest arithmetic slices of the array, then compute the number of slices. Move to next start position, and do it again. 

Time complexity: O(N)
"""
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        if len(A) <= 2:
            return ans
        pos_P = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] != A[pos_P + 1] - A[pos_P]:
                # break of arithmetic slice
                k = i - pos_P
                ans += (k - 1) * (k - 2)//2
                pos_P = i - 1
        k = len(A) - pos_P
        ans += (k - 1) * (k - 2)/2
        return ans