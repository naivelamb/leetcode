"""
https://leetcode.com/problems/majority-element-ii/

There are at most two elements to be returned.

Boyer-Moore majority vote algorithm.
In the first pass, we have two values: a candidate and a count. If we find a number the same as the candidate, increment count by 1, else decrement count by 1.
If the count is 0, we set candidate as the current number.

In the 2nd pass, we need to examine whether the candidate meets the requirement.

Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        cand1, cand2, cnt1, cnt2 = None, None, 0, 0
        for n in nums:
            if cand1 == n:
                cnt1 += 1
            elif cand2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = n
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = n
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ans = []
        for c in [cand1, cand2]:
            if nums.count(c) > len(nums) // 3:
                ans.append(c)
        return ans
