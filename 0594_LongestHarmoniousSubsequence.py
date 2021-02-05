"""
https://leetcode.com/problems/longest-harmonious-subsequence/

Get count of all elements, check +1/-1 count for all possible values.
Timec complexity: O(N)
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        ans = 0
        for n in cnt:
            if n + 1 in cnt:
                ans = max(ans, cnt[n] + cnt[n+1])
            if n - 1 in cnt:
                ans = max(ans, cnt[n] + cnt[n - 1])
        return ans