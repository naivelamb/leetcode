# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/all-paths-from-source-to-target/

DFS + backtracking
"""
class Solution:
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
        self.res = []
        N = len(graph)
        visited = {}
        visited[0] = 1
        self.dfs(graph, N - 1, visited, [0])
        return self.res
    
    def dfs(self, graph, target, visited, path):
        if path[-1] == target:
            self.res.append(path[:])
            return
        for i in graph[path[-1]]:
            if i not in visited:
                visited[i] = 1
                self.dfs(graph, target, visited, path + [i])
                del visited[i]
                
graph = [[1,2], [3], [3], []] 
s = Solution()
print(s.allPathsSourceTarget(graph))