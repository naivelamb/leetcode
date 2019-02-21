# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/largest-number/

Customized sort. 
"""
class LargerNumkey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumkey))
        return '0' if largest_num[0] == '0' else largest_num