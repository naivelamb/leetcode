"""
https://leetcode.com/problems/russian-doll-envelopes/

DP[i] => most envelops ending with envelopes[i]
Naive thought would be sort envelopes, then find DP. Time complexity would be O(N^2).

If envelopes are sorted by (x[0], -x[1]), then we only need to find the longest increased subsequence for x[1]. 
Let dp record the height sequence of envelope. We try to find the position we can put the height in to the envelope. We only attached the envelope when we are at the end of dp (height larger than all heights). Time complexity would be O(NlogN).


Time complexity: O(NlogN)
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp): dp.append(height)
            else: dp[left] = height
        return len(dp)