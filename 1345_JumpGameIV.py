"""
https://leetcode.com/problems/jump-game-iv/

Build a graph, where i and j are connected if:
1). i == j + 1
2). i == j - 1
3). arr[i] == arr[j]
Then BFS.

Time complexity: O(N), since each node is visited at most once. 
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        vals = collections.defaultdict(list)
        for i, x in enumerate(arr):
            vals[x].append(i)

        q = collections.deque()
        q.append([0, 0])
        visited = set()
        N = len(arr)
        while q:
            node, step = q.popleft()
            if node == N - 1:
                return step
            for child in [node - 1, node + 1]:
                if 0 <= child < N and child not in visited:
                    q.append([child, step + 1])
                    visited.add(child)
            for j in vals[arr[node]]:
                if j != node and j not in visited:
                    q.append([j, step + 1])
                    visited.add(j)
            vals[arr[node]].clear()