"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/
1) Binary Search.
For each row, use binary search to find the left most index with 1. -> O(logm)
Go through each row. ans = -1
if ans == -1 or left_idx == -1  ==> ans = max(ans, left_idx)
else == > ans = min(ans, left_idx)
Time complexity: O(nlogm)

2) Start from the right most corner. If postiion is 0, we move down; if position is 1, we move left. Stop if we have no more move.
Time complexity: O(mn)
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        ans = -1
        def binary_search(i):
            l, r = 0, m - 1
            while l <= r:
                mid = (l+r) // 2
                if binaryMatrix.get(i, mid) == 1:
                    if mid == 0 or binaryMatrix.get(i, mid-1) == 0:
                        return mid
                    else:
                        r = mid - 1
                else:
                    l = mid + 1
            return -1
        for i in range(n):
            left_idx = binary_search(i)
            if ans == -1 or left_idx == -1:
                ans = max(ans, left_idx)
            else:
                ans = min(ans, left_idx)
        return ans

    def leftMostColumnWithOne1(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        ans = -1
        r, c = 0, m - 1
        while r < n and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                ans = c
                c -= 1
            else:
                r += 1
        return ans
