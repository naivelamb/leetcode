"""
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Lower bound is 1, larger bound is max(nums). There is a linear relation between divisor and the summation: larger divisor, smaller summation. Hence we can use binary search to find the divisor. 

Time complexity: O(NlogM), N = len(nums), M = max(nums)
"""
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            res = sum([math.ceil(x/mid) for x in nums])
            if res > threshold: # divisor too small
                # check (mid + 1) as divisor
                res2 = sum([math.ceil(x/(mid + 1)) for x in nums])
                if res2 < threshold:
                    return mid + 1
                else:
                    l = mid + 1
            else:
                r = mid - 1
        return l