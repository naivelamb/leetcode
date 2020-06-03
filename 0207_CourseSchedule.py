"""
https://leetcode.com/problems/course-schedule/

Build the graph, if there is circle in the graph, return False.

graph[i] = [a, b, c] => Course-i are the prerequisites of [a, b, c]

Time complexity: O(E + V**2)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # build graph
        self.graph = collections.defaultdict(set)
        for i, j in prerequisites:
            self.graph[j].add(i)

        # find circle
        # 0 -> unvisited
        # 1 -> visited via other path
        # -1 -> visited in current path (circle)
        self.state = [0] * numCourses
        for node in range(numCourses):
            if self.dfs(node):
                return False
        return True

    def dfs(self, node):
        # return True if find circle
        if self.state[node] == 1:
            return False
        if self.state[node] == -1:
            return True
        self.state[node] = -1
        for nei in self.graph[node]:
            if self.dfs(nei):
                return True
        self.state[node] = 1
        return False
