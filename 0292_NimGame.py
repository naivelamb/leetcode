# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/nim-game/

If the stone left can be divisible by 4, then you will lose.
"""
class Solution:
    def canWinNim(self, n: 'int') -> 'bool':
        return (n % 4 != 0)
