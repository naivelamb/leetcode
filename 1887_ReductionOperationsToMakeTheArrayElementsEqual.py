"""
https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
Cumulative count number of nums larger than next large elements. 

Time complexity: O(nlogn)
"""
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        if len(cnt) == 1:
            return 0
        vals = sorted(cnt.keys(), reverse=True)
        p_sum = [0]
        for v in vals[:-1]:
            p_sum.append(p_sum[-1] + cnt[v])
        return sum(p_sum)
        