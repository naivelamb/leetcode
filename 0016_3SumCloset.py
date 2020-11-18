"""
https://leetcode.com/problemset/all/

Brute force takes O(N^3).

If we are facing a sorted array, we can fix the starting point (try all possibilities in range[0, n-2]), then use two pointers to find the closes results O(N). ==> O(N^2) 

Time complexiy: O(NlogN + N^2) = O(N^2)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == target:
                    return sums
                elif sums < target:
                    j += 1
                else:
                    k -= 1
                
                if abs(sums - target) < abs(res - target):
                    res = sums
        return res