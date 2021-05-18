"""
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

Binary search.

O(mlogn)
"""
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        nums3 = nums2[::-1]
        n = len(nums2)
        for i, x in enumerate(nums1):
            if i >= n or nums1[i] > nums2[i]:
                continue
            j = n - bisect.bisect_left(nums3, x) - 1
            #print(i, j)
            ans = max(j-i, ans)
        return ans
            