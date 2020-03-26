"""
https://leetcode.com/problems/all-paths-from-source-to-target/

If cycle exists, return False.
No cycle, check all possible paths.
"""
class Solution:
    def leadsToDestination(self, n: int, edges, source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)

        if graph[destination]:
            return False

        visited = set()
        def dfs(node): # return True if all path from node leads to destination
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)

            if node not in graph:
                return False

            res = True
            for nei in graph[node]:
                x = dfs(nei)
                visited.discard(nei)
                if not x:
                    return False
            return res

        return dfs(source)

sol = Solution()
assert sol.leadsToDestination(3, [[0,1],[0,2]], 0, 2) == False
assert sol.leadsToDestination(4, [[0,1],[0,3],[1,2],[2,1]], 0, 3) == False
assert sol.leadsToDestination(4, [[0,1],[0,2],[1,3],[2,3]], 0, 3) == True
assert sol.leadsToDestination(3, [[0,1],[1,1],[1,2]], 0, 2) == False
assert sol.leadsToDestination(2, [[0,1],[1,1]], 0, 1) == False
