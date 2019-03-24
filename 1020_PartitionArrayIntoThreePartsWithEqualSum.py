# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

Let total = sum(A), if total % k != 0, return false. 
Target = total // 3
Now just check whether we can find 3 subarrays whose sum is target.

Time complexity: O(n)
"""
class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        target = sum(A) // 3
        sub_sum, cnt = 0, 0
        for x in A:
            sub_sum += x
            if sub_sum == target:
                sub_sum = 0
                cnt += 1
        return cnt == 3
