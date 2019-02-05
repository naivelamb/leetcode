# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-average-subarray-ii/

#1 Brute force
Try all possible k and calculte the average find the maximum one. O(n^2)

#2 Binary Search average
Let x = (min(nums) + max(nums)) / 2
If we can find a subarray of length greater than k with average >= x, we search
next x in the range of [x, max(nums)]. Else, in the range of [min(nums), x]

How can we determin whether we have a subarray of length greater than k with 
average >= x?
nums[i] + nums[i+1] + ... + nums[j] >= x * (j - i + 1)
which is the same as,
(nums[i] - x) + (nums[i+1] - x) + ... + (nums[j] - x) >= 0, j - i >= k
So we need to check for a transformed array (nums[i] - x), whether there is a 
subarray with length >= k having average >= x.

This can be done in linear time. We start with getting sum(nums[:k]) - x * k, if
this is >= 0, return True. 
If it is not >= 0, we need to check prefix sum. 
Let prefix_sum[i] = sum(nums[:i]) - i * x
We keep track of two values:
    1. A = sum(nums[:j]) - j * x, where j >= k
    2. B = min(prefix_sum[i]), for 0 <= i <= (j - k)
Return True if A - B >= 0
"""
class Solution:
    def findMaxAverage_TLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = float('-inf')
        for s in range(len(nums) - k + 1):
            total = 0
            for i in range(s, len(nums)):
                total += nums[i]
                if i - s + 1 >= k:
                    res = max(res, total/(i-s+1))
        return res
    
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        lo, hi = min(nums), max(nums)
        precision = 1E-6
        while hi - lo > precision:
            mid = (lo + hi) / 2
            if self.findSubarray(mid, nums, k):
                lo = mid
            else:
                hi = mid
        return lo
        
    def findSubarray(self, mid, nums, k):
        subarray_sum = sum(nums[:k]) - k * mid
        if subarray_sum >= 0:
            return True
        prev, min_prev = 0, 0
        for i in range(k, len(nums)):
            subarray_sum += nums[i] - mid
            prev += nums[i - k] - mid
            min_prev = min(prev, min_prev)
            if subarray_sum >= min_prev:
                return True
        return False
    
nums = [1, 12, -5, -6, 50, 3]
k = 4
s = Solution()
print(s.findMaxAverage_TLE(nums, k))