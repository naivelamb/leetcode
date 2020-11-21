"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Binary search. 

Everytime we select a mid, one of [l, mid], [mid, r] will be sorted. 

We first move l until nums[l] != nums[mid],
if nums[mid] >= nums[l] ==> [l, mid] is sorted, we check whether target is in this range. 
Else ==> [mid, r] is sorted, we check whether target is in this range. 

Time complexity: Worst case O(N), best case O(logN)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            while l < mid and nums[l] == nums[mid]:
                l += 1
            
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False