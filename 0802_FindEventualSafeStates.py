"""
https://leetcode.com/problems/find-eventual-safe-states/

We need to find all nodes belong to circle in the directed graph.

DFS + state for each node.
0 -> unvisited
1 -> visiting
2 -> visited and safe

DFS return True if the node is "safe".
For a non-fresh node, we check whether the state is 2.

Assign the unvisited node with state 1.
For all the neighbors,
1). if state[nei] == 2, continue
2). if state[nei] == 1 or not dfs(nei): return False

After checking all the neighbors, state[nei] = 2, return True

Time complexity: O(N + E), N = # of nodes, E = # of edges
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = [0] * len(graph)

        def dfs(node):
            if state[node] != 0:
                return state[node] == 2

            state[node] = 1
            for nei in graph[node]:
                if state[nei] == 2:
                    continue
                if state[nei] == 1 or not dfs(nei):
                    return False
            state[node] = 2
            return True

        ans = []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans
