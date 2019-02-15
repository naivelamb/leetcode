# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 18:20:31 2019

We know the length of the longest increasing subsequence can be got by dp, where dp[i] is the length of the longest subsequence ending at nums[i]. 

To get the count, we need another dp array count, where count[i] is the number of longest increasing subsequence ending at nums[i]. 

If dp[i] >= dp[j], then dp[j] = 1 + dp[i], count[j] = count[i]
If dp[i] + 1 == dp[j], then count[j] += count[i]

Finally, we need to find the index ending at which we have longest subsequence, then sum all of them. 
"""
class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        if n <= 1: return n
        dp, cnt = [1] * n, [1] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if dp[i] >= dp[j]:
                        dp[j] = 1 + dp[i]
                        cnt[j] = cnt[i]
                    elif dp[i] + 1 == dp[j]:
                        cnt[j] += cnt[i]
        longest = max(dp)
        return sum(cnt[i] for i in range(n) if dp[i] == longest)

s = Solution()
nums = [2, 2, 2, 2, 2]
print(s.findNumberOfLIS(nums))