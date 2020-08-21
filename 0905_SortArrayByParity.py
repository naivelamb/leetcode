"""
https://leetcode.com/problems/sort-array-by-parity/

Two pointer: left and right.
Switch if A[l] % 2 == 1 and A[r] % 2 == 0
Else, l += 1, r -= 1

Time Complexity: O(N)
Space Complexity: O(1)
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] % 2 == 1 and A[r] % 2 == 0:
                A[l], A[r] = A[r], A[l]
            if A[l] % 2 == 0:
                l += 1
            if A[r] % 2 == 1:
                r -= 1
        return A
