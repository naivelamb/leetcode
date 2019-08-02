#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/push-dominoes/

#1 Brute force
Find the first L/R at the head/tail, then decide how to deal with the non-
dominoes at head/tail. 

Then find L/R pairs, and decide how to deal with the dominoes in between. 
Time complexity: O(n)
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        head, tail, n = 0, len(dominoes) - 1, len(dominoes)
        
        # search starting L/R, deal with head/tail
        while head < n and dominoes[head] == '.':
            head += 1
        if head < n and dominoes[head] == 'L':
            dominoes[:head] = ['L'] * head
        while tail >= 0 and dominoes[tail] == '.':
            tail -= 1
        if tail >= 0 and dominoes[tail] == 'R':
            dominoes[tail:] = ['R'] * (len(dominoes) - tail)
            
        prev = head
        for i in range(head+1, tail+1):
            if dominoes[i] == 'L':
                if dominoes[prev] == 'L':
                   dominoes[prev:i] = ['L'] * (i - prev) 
                else:
                    mid = (prev + i) // 2
                    if (prev + i) % 2 == 0:
                        dominoes[prev:mid] = ['R'] * (mid - prev)
                        dominoes[mid+1:i] = ['L'] * (i - mid - 1)
                    else:
                        dominoes[prev:mid+1] = ['R'] * (mid - prev + 1)
                        dominoes[mid+1:i] = ['L'] * (i - mid - 1)
                prev = i
            elif dominoes[i] == 'R':
                if dominoes[prev] == 'R':
                    dominoes[prev:i] = 'R' * (i - prev)
                prev = i
        return ''.join(dominoes)

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