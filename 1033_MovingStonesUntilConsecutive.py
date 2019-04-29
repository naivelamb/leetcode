# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/moving-stones-until-consecutive/

Sort (a, b, c) to find (x, y, z)
Then need to find the difference between x, y and z. 
Max must be move x and z to y in the step of 1, so it is 
(z - y - 1) + (y - x - 1) = z - x - 2
Min depends. For general cases (y - x > 2, z - y > 2), it is 2. 
If y - x == 1 and z - y == 1, it is 0
If (y - x) == 2 or z - y == 2, it is 1 
If only one of (y - x, z - y) is 1, it is 1.
"""
class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        x, y, z = sorted([a, b, c])
        if x + 1 == y and y + 1 == z:
            return [0, 0]
        ans_min, ans_max = 2, z - x - 2
        if y - x == 1 or z - y == 1:
            ans_min -= 1
        elif y - x == 2 or z - y == 2:
            ans_min -= 1
        return [ans_min, ans_max]