"""
https://leetcode.com/problems/flipping-an-image/
"""
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for row in A:
            row = row[::-1]
            res.append([1-x for x in row])
        return res