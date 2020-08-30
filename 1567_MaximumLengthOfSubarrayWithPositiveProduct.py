"""
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Count the max length of positive & negative subarray ending at current position.

val == 0: pos = neg = 0
val > 0: pos += 1, neg += 1 if neg != 0
val < 0: new_neg = pos + 1, if old_neg == 0: new_pos = 0 else new_pos = old_neg + 1
"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for i, val in enumerate(nums):
            if val == 0:
                pos = neg = 0
            elif val > 0:
                pos += 1
                if neg != 0:
                    neg += 1
            else:
                new_neg = pos + 1
                if neg == 0:
                    pos = 0
                else:
                    pos = neg + 1
                neg = new_neg
            ans = max(ans, pos)
        return ans
