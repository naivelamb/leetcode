#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/lemonade-change/

#1 Greedy

Always give the larger bill for change. Store the current bill in a dict. 

Time complexity: O(N)
"""
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ref = {5 : 0,
               10: 0,
               20: 0}
        for bill in bills:
            if bill == 5:
                ref[bill] += 1
            else:
                change = bill - 5
                need_10 = change // 10
                if need_10 <= ref[10]:
                    ref[10] -= need_10
                    change -= need_10 * 10
                else:
                    ref[10] = 0
                    change -= ref[10] * 10
                need_5 = change // 5
                if need_5 <= ref[5]:
                    ref[5] -= need_5
                    ref[bill] += 1
                else:
                    return False
        return True
    

test = [
        [5,5,5,10,20],
        [5,5,10],
        [10,10],
        [5,5,10,10,20],
        ]
ans = [
       True,
       True,
       False,
       False,
       ]

sol = Solution()
for t, a in zip(test, ans):
    sol0 = sol.lemonadeChange(t)
    print(sol0, a)