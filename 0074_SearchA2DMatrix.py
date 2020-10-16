"""
https://leetcode.com/problems/search-a-2d-matrix/

Binary Search based on first element of each row to locate row index, then binary search on the row to find col index.

Time complexity: O(logMN)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search_col(nums, target):
            if target < nums[0]:
                return -1

            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        return mid
                    else:
                        l = mid + 1
                else:
                    r = mid - 1
            return -1

        def binary_search_row(nums, target):
            if target < nums[0] or target > nums[-1]:
                return False

            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        col_nums = [matrix[i][0] for i in range(m)]
        row = binary_search_col(col_nums, target)
        print(row)
        if row == -1:
            return False
        else:
            return binary_search_row(matrix[row], target)
