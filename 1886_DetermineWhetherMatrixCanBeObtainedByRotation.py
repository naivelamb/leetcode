"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Rotate and check. 
O(mn)
"""
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(3):
            if mat == target:
                return True
            mat = [list(x[::-1]) for x in zip(*mat)]
        return mat == target