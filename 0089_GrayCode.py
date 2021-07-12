"""
https://leetcode.com/problems/gray-code/

gray code mirror

1-bit:  0 1  
mirror: 0 1 1 0
2-bit:  00 01 11 10
mirror: 00 01 11 10 10 11 01 00
3-bit:  000 001 011 010 110 111 101 100
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 3, 2]
        else:
            return self.grayCode(n-1) + [x + (2**(n-1)) for x in self.grayCode(n-1)[::-1]]
