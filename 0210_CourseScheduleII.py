# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/course-schedule-ii/

We need to check whether there is a circle in the graph, otherwise return the 
sorted order. => topological sort. 

Starting from a node, we search the path. Each node has three state: visited,
visiting (in currrent search) and unvisited.
If we are visiting a 'visiting' node, there is a circle.

Time complexity: O(n) => every node is visited once.
"""
import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # build the graph
        self.graph = collections.defaultdict(set)         
        for pair in prerequisites:
            self.graph[pair[1]].add(pair[0])
        
        self.ans = []
        # 0 -> unvisited, 1 -> visited, -1 -> visiting
        self.state = [0] * numCourses
        
        for node in range(numCourses):
            if self.dfs(node):
                return []
        return self.ans[::-1]
    
    def dfs(self, node):
        # return True if find loop
        if self.state[node] == -1:
            return True
        if self.state[node] == 1:
            return False
        # visiting an unvisited node
        self.state[node] = -1
        for nei in self.graph.get(node, []):
            if self.dfs(nei):
                return True
        self.state[node] = 1
        self.ans.append(node)
        
s = Solution()
n = 4
pairs = [[1,0],[2,0],[3,1],[3,2]]
print(s.findOrder(n, pairs))