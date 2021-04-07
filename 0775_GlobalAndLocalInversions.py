"""
https://leetcode.com/problems/global-and-local-inversions/

All local inversions are global inversions. 
If num of local inversions is equal to global inversions, it means any new number added introduce equal amount of local inversion and global inversion.
It means we cannot find A[i] > A[j] with i + 2 <= j
"""
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i+2]: return False
        return True