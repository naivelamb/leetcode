"""
https://leetcode.com/problems/maximum-population-year/

Build an array to record number of people each year.
"""
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        states = [0] * 101
        for l, r in logs:
            for i in range(l-1950, r-1950):
                states[i] += 1
        
        v = max(states)
        for i, x in enumerate(states):
            if x == v:
                return i + 1950