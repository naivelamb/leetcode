"""
https://leetcode.com/problems/the-maze/

DFS, use while to find the entry point of next recursion, since the ball can only change direction when hitting wall.
Time complexity: O(mn); (m, n) = shape of maze
"""
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.visited = set()
        def dfs(i, j, maze, destination):
            if i == destination[0] and j == destination[1]:
                return True
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i, j
                while 0 <= new_i + di < len(maze) and 0 <= new_j + dj < len(maze[0]) and maze[new_i + di][new_j + dj] == 0:
                    new_i, new_j = new_i + di, new_j + dj
                if (new_i, new_j) not in self.visited:
                    self.visited.add((new_i, new_j))
                    if dfs(new_i, new_j, maze, destination):
                        return True
            return False
        return dfs(start[0], start[1], maze, destination)
