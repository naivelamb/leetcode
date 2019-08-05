#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/push-dominoes/

#1 Brute force
L..L or R...R -> set all dots to be L or R
R..L/R...L -> RRLL/RR.LL
L..R -> L..R
Find all neighbor symbols and modify the dots.

Time complexity: O(N)

"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        
        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y: # RL
                dots = j - i - 1
                ans[i+1:i+1+dots//2] = ['R'] * (dots//2)
                ans[j-dots//2:j] = ['L'] * (dots//2)
        return ''.join(ans)

    def pushDominoes_stack(self, dominoes: str) -> str:
        dominoes = list('L' + dominoes + 'R')
        left, right = [], []
        for i, ch in enumerate(dominoes):
            if ch == 'R':
                right.append(i)
            if ch == 'L':
                left.append(i)
        
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if right[r] < left[l]: # R....L
                dots = (left[l] - right[r] - 1) // 2
                dominoes[right[r]+1: right[r] + dots+1] = ['R'] * dots
                dominoes[left[l] - dots: left[l]] = ['L'] * dots
                l += 1
                r += 1
            else:
                l += 1
        return ''.join(dominoes[1:-1])


test = [
        ".",
        "R...L",
        ".L.R...LR..L..",
        "RR.L",
        ]
ans = [
       ".",
       "RR.LL",
       "LL.RR.LLRRLL..",
       "RR.L",
       ]

sol = Solution()
for t, a in zip(test, ans):
    sol0 = sol.pushDominoes(t)
    print(sol0)
    print(a)