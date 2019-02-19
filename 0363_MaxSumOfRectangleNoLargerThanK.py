# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:15:31 2019

If we have a 1-D array, the maximum sum of subarray can be get in O(n).
Cur_max, max_sum = nums[0], nums[0]
for i in range(1, len(nums):
	Cur_max = max(cur_max + nums[i], nums[i])
	Max_sum = max(max_sum, cur_max)

For the 2D matrix, if we know the starting row, and ending row, each the sums 
can be collapsed to a 1-D array, and we can apply the 1D version to get the 
maximum sum. 

To get the maximum sum <= K, we will use merge sort to get it. 

Assume we have m-row and n-col, then we have m^2*n 1D arrays, whose size is n. 
The merge sort takes nlogn to find the value.

Therefore, the overall time complexity is O(m^2*nlogn)
"""
class Solution:
    def maxSumSubmatrix(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        m, n = len(matrix), len(matrix[0])
        M, N = min(m, n), max(m, n)
        ans = -float('inf')
        
        def findMaxArea(sums, l, r):
            # return max-val such that val <= K
            if l + 1 >= r:
                return -float('inf')
            mid = (l + r) // 2
            res = max(findMaxArea(sums, l, mid), findMaxArea(sums, mid, r))
            i, j = 0, mid
            while i < mid and j < len(sums):
                if sums[j] - sums[i] <= k:
                    res = max(res, sums[j] - sums[i])
                    j += 1
                i += 1
            sums[l:r] = sorted(sums[l:r])
            return res
        
        for i1 in range(M):
            tmp = [0] * N
            for i2 in range(i1, M):
                sums, low, maxArea = [0], 0, -float('inf')
                for j in range(N):
                    tmp[j] += matrix[i2][j] if m <= n else matrix[j][i2]
                    sums.append(sums[-1] + tmp[j])
                    maxArea = max(maxArea, sums[-1] - low)
                    low = min(low, sums[-1])
                if maxArea <= ans:
                    continue
                elif maxArea == k:
                    return k
                else:
                    maxArea = findMaxArea(sums, 0, N + 1)
                ans = max(maxArea, ans)
            return ans
s = Solution()
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(s.maxSumSubmatrix(matrix, k))
