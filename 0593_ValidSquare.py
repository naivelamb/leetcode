# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/valid-square/

Sort the 4 points, then the square can only formd by using (1, 2) and (1, 3), 
(2, 4), (3, 4) as 4 points. Then check the length of 4 sides and 2 diagonals. 

Time complexity: O(1)
"""
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        points = [tuple(x) for x in [p1, p2, p3, p4]]
        if len(set(points)) != 4: # make sure there are 4 distinct points.
            return False
        points.sort()
        p12 = (points[0][0] - points[1][0], points[0][1] - points[1][1])
        p34 = (points[2][0] - points[3][0], points[2][1] - points[3][1])
        p13 = (points[0][0] - points[2][0], points[0][1] - points[2][1])
        p24 = (points[1][0] - points[3][0], points[1][1] - points[3][1])
        p14 = (points[0][0] - points[3][0], points[0][1] - points[3][1])
        p23 = (points[1][0] - points[2][0], points[1][1] - points[2][1])
        
        length = [x[0]**2 + x[1]**2 for x in [p12, p34, p13, p24, p14, p23]]
        
        flag_side = (length[0] == length[1] == length[2] == length[3])
        flag_diag = (length[4] == length[5])
        flag_tri = (length[0] * 2 == length[4])
        if flag_side and flag_diag and flag_tri:
            return True
        else:
            return False
