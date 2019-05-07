# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

# Search
Use DFS/BFS to search from (x, y), find the most left, right, top, bottom pixel, 
and the area is (right - left) * (bottom - top).
Time complexity: O(mn)

# Binary Search
Since there is only one black region, we can use binary search to find the top/
bottom row, left/right column. 
Top in the search range row (0, x), first row has '1'.
Bottom in the search range row (x + 1, m), last row has '1'.
Left in the search range column (0, y), first col has '1'.
Right in the search range column (y + 1, n), last col has '1'.
Time complexity: O(m*log(n) + n*log(m))

"""
import collections
class Solution:
    def minArea_BFS(self, image, x, y):
        m, n = len(image), len(image[0])
        left, right = n - 1, 0
        top, bottom = m - 1, 0
        queue = collections.deque([(x, y)])
        visited = {(x, y)}
        while queue:
            i, j = queue.popleft()
            top, bottom = min(i, top), max(i, bottom)
            left, right = min(j, left), max(j, right)
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    if image[new_i][new_j] == '1' and (new_i, new_j) not in visited:
                        queue.append((new_i, new_j))
                        visited.add((new_i, new_j))
        return (right - left + 1) * (bottom - top + 1)                    
            
    def minArea(self, image, x, y):
        def searchRows(image, i, j, flag_first):
            while i != j:
                mid = (i + j) // 2
                if ('1' in image[mid]) == flag_first:
                    j = mid
                else:
                    i = mid + 1
            return i
        
        def searchColumns(image, i, j, top, bottom, flag_first):
            while i != j:
                mid = (i + j) // 2
                if any(image[k][mid] == '1' for k in range(top, bottom)) == flag_first:
                    j = mid
                else:
                    i = mid + 1
            return i
        
        top = searchRows(image, 0, x, True)
        bottom = searchRows(image, x + 1, len(image), False)
        left = searchColumns(image, 0, y, top, bottom, True)
        right = searchColumns(image, y+1, len(image[0]), top, bottom, False)
        return (bottom - top) * (right - left)
        