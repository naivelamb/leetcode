"""
https://leetcode.com/problems/jump-game-iii/

BFS
Time complexity: O(N)
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = collections.deque()
        queue.append(start)
        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            if arr[curr] == 0:
                return True
            visited.add(curr)
            if curr + arr[curr] < len(arr):
                queue.append(curr + arr[curr])
            if curr - arr[curr] >= 0:
                queue.append(curr - arr[curr])
        return False
    
    def canReachDFS(self, arr, start):
        visited = set()
        def dfs(pos):
            if pos >= len(arr) or pos < 0:
                return False
            if pos in visited:
                return
            if arr[pos] == 0:
                return True
            visited.add(pos)
            left, right = pos - arr[pos], pos + arr[pos]
            if dfs(left) or dfs(right):
                return True
            return False
        return dfs(start)