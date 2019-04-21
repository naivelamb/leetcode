# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/two-city-scheduling/

Compute the difference between costs to the two cities for all people, sort it. 
First half go to A city, second half go to B city.

Time compleixty: O(nlogn)
"""
class Solution:
    def twoCitySchedCost(self, costs):
        N = len(costs)
        tmp = sorted([(costs[i][0] - costs[i][1], i) for i in range(N)])
        res = 0
        for i, x in enumerate(tmp):
            if i < N//2:
                res += costs[x[1]][0]
            else:
                res += costs[x[1]][1]
        return res