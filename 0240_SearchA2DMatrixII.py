"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

1) Binary Search
For row search, we can do binary search.
Check row by row.

Time complexity: O(mlogn)

2) Linear Search
If matrix[r][c] > target, then all matrix[r][c:] > target; matrix[r:][c] > target.
We can go from the bottom left corner,
if matrix[r][c] > target, we move up;
if matrix[r][c] < target, we move right.

Time complexity: O(m + n)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(vals, target):
            if target < vals[0] or target > vals[-1]:
                return False
            l, r = 0, len(vals) - 1
            while l <= r:
                mid = (l + r) // 2
                if vals[mid] == target:
                    return True
                elif vals[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        m = len(matrix)
        for i in range(m):
            if target < matrix[i][0] or target > matrix[i][-1]:
                continue
            else:
                if binary_search(matrix[i], target):
                    return True
        
        return False

    def searchMatrix_linear(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        while r >= 0 and c < n:
            current = matrix[r][c]
            if current == target:
                return True
            elif current > target:
                r -= 1
            else:
                c += 1
        return False