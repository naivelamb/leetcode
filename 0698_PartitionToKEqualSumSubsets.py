# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

With k, we know the sum of each subsets should be sum(nums) // k. 
If sum(nums) % k != 0 or sum(nums) < k, return False. 

Then we can try to add numbers to get the target, if so we mark all used nums 
(k - 1) and keep looking for next subsets. Return True if current subsest sum 
equals to target and k == 1. This part can be done recursively. 

"""
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0 or k > sum(nums):
            return False
        # get target
        target = sum(nums) // k
        # mark whether a num has been used
        used = [0] * len(nums)
        def dfs(k, from_index, cur_sum):
            # Return True if given the current sum and from_index, we can get 
            # k equal subsets. 
            #Last subset
            if k == 1 and cur_sum == target: 
                return True
            # k != 1 => not last subset, keep looking
            if cur_sum == target: 
                return dfs(k-1, 0, 0)
            # cur_sum != target, try to build subsets
            for i in range(from_index, len(nums)): 
                if cur_sum + nums[i] <= target and not used[i]:
                    used[i] = 1
                    if dfs(k, i+1, cur_sum + nums[i]):
                        return True
                    used[i] = 0
            return False
        
        return dfs(k, 0, 0)
