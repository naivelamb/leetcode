# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/split-array-largest-sum/

#1 DP. 
dp[i][j] => minimum largest sum of subarrays after spliting nums[:i] into j non-
empty subarrays.
Then dp[i][j] = min(max(dp[k][j-1], sum(nums[k+1:i])) for k in range(0, i))
Return dp[n][m]
Time complexity: O(n^2*m)

#2 Binary Search
The answer must be in the range of [max(nums), sum(nums)]. We search the answer.
Given a candidate C, compute the number of groups k needed.

if k > m: # C too small
    l = C + 1
else:
    r = C

Time complexity: O(nlog(sum(nums)))
"""
class Solution:
    def splitArray(self, nums, m):
        n = len(nums)
        pre = [0] # prefix sum
        for x in nums:
            pre.append(pre[-1] + x)
        
        INF = float('inf')
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], pre[i] - pre[k]))
        return dp[n][m]
    
    def splitArray_bs(self, nums, m):
        def is_valid(nums, m, mid):
            # find at least how many sub-sum are smaller than mid by greedy partition
            # Time Complexity； O(n)
            cnts, curr_sum = 0, 0
            for x in nums:
                curr_sum += x
                if curr_sum > mid:
                    cnts, curr_sum = cnts + 1, x
            subs = cnts + 1
            return subs <= m
        
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low + high) // 2
            if is_valid(nums, m, mid):
                ans, high = mid, mid - 1
            else:
                low = mid + 1
        return ans
    
s = Solution()
nums = [7,2,5,10,8]
m = 2
print(s.splitArray(nums, m))
print(s.splitArray_bs(nums, m))