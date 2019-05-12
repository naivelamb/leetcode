# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/flower-planting-with-no-adjacent/

Build the graph. Check the neighbor garden flowers, place the first available 
flower. 

Time complexity: O(n). Because we have finite neighbors (3) and finite flowers (4)
"""
import collections
class Solution:
    def gardenNoAdj(self, N, paths):
        # build graph
        graph = collections.defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        ans = [0] * N
        ref = {}
        for i in range(N):
            used_flowers = set()
            for nei in graph[i + 1]:
                if nei in ref:
                    used_flowers.add(ref[nei])
            
            cand = [x for x in range(1, 5) if x not in used_flowers]
            ans[i] = cand[0]
            ref[i + 1] = cand[0]
        return ans