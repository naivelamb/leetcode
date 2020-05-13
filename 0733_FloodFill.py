"""
https://leetcode.com/problems/flood-fill/

BFS, time complexity O(mn)

"""
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        m, n = len(image), len(image[0])
        queue = collections.deque([(sr, sc)])
        color = image[sr][sc]
        image[sr][sc] = newColor
        visited = set(queue)
        while queue:
            i, j = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i + di, j + dj
                if (0 <= new_i < m) and (0 <= new_j < n) and image[new_i][new_j] == color and (new_i, new_j) not in visited:
                    image[new_i][new_j] = newColor
                    visited.add((new_i, new_j))
                    queue.append((new_i, new_j))
        return image

sol = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
assert sol.floodFill(image, sr, sc, newColor) == [[2,2,2],[2,2,0],[2,0,1]]
