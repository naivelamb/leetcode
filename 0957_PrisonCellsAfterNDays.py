# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/prison-cells-after-n-days/submissions/

Cell.length == 8, there are at most 2**8 = 256 possible cells. 
If N > 256, there must be repeatition. 
So we need to find the circle period, then just match it.

Time Complexity: O(2^n), n = len(cells)
"""
class Solution:
    def prisonAfterNDays(self, cells: 'List[int]', N: 'int') -> 'List[int]':
        def nextday(cells):
            # given current cells, generate cells next day
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) 
                    for i in range(len(cells))]
        
        # seen: key is cells, val is the first appearance day
        # ref: key is the first appearance day, val is cells
        # i: ith-day
        seen, ref = {}, {}
        ans = []
        
        for i in range(N):
            c = tuple(cells)
            # find circle
            if c in seen:
                start = seen[c] # where circle start
                period = i - start # length of the circle
                loci = (N - i + 1) % period - 1 # location of the end
                if loci == -1:
                    loci += period
                ans = ref[loci + start]
                break
            seen[c] = i
            ref[i] = cells
            cells = nextday(cells)
        else:
            ans = cells
        return ans