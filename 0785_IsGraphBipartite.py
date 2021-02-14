"""
https://leetcode.com/problems/is-graph-bipartite/
Color the current node, then give another color to next node. 
Time Complexity: O(V+E)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                stack = [i]
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = 1 - color[node]
                            stack.append(nei)
                        else:
                            if color[nei] == color[node]:
                                return False
        return True

    def isBipartite_dfs(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(pos):
            #return True if we can paint all associated node
            #else False
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True        