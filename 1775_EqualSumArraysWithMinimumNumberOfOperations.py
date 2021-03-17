"""
https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

First rule out the case we cannot make them equal. 

To find the number of operations, we do it in a greedy way. 
To make smaller larger, we always try to make the smallest element to the largest.
To make larger smaller, we always try to make the largest element to the smallest.

Time complexity: O(mlogm + nlogn)
"""
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums1) < len(nums2) or sum(nums2) < len(nums1):
            return -1

        s1, s2 = sum(nums1), sum(nums2)
        if s1 < s2: # make sure s1 >= s2
            nums1, nums2 = nums2, nums1
        s1, s2 = sum(nums1), sum(nums2) 

        nums1.sort()
        nums2.sort()

        i, j = len(nums1) - 1, 0
        ans = 0
        while s1 > s2:
            if j >= len(nums2) or (0 <= i and nums1[i] - 1 > 6 - nums2[j]):
                s1 += 1 - nums1[i]
                i -=1
            else:
                s2 += 6 - nums2[j]
                j += 1
            ans += 1
        return ans