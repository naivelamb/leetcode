# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/generalized-abbreviation/submissions/

Backtracking

Time complexity: O(n2^n) => 2^n possitiblities, build string takes O(n)
"""

class Solution:
    def generateAbbreviations(self, word: str):
        def helper(word, pos, cur, cnt, result):
            if pos == len(word):
                result.append(cur + (str(cnt) if cnt > 0 else ""))
            else:
                # current position in abbreviation
                helper(word, pos + 1, cur, cnt + 1, result)
                # keep current position
                helper(word, pos + 1, cur + (str(cnt) if cnt > 0 else "") + word[pos], 0, result)
        
        result = []
        helper(word, 0, "", 0, result)
        return result