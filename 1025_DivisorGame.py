# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/divisor-game/

If n is even, then Alice must win.
If n is odd, then Alice must loss
"""
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0