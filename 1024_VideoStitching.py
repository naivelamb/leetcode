# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/video-stitching/

Scan twice, greedy.
dp[i] => start from i, max coverage
dp2[i] => start from j <= i, max coverage

Time complexity: O(n) + O(T), n -> len(clips)
"""
class Solution:
    def videoStitching(self, clips, T):
        dp = {} # start from i, max coverage
        state = [0] * 101 # max length is 101
        for clip in clips:
            l, r = clip
            dp[l] = max(dp.get(l, 0), r)
            state[l:r+1] = [1] * (r - l + 1)
            
        if sum(state[:T+1]) != T + 1:
            return -1
        
        dp2 = {} # start from j <= i, max coverage
        max_reach = 0
        for i in range(T + 1):
            max_reach = max(max_reach, dp.get(i, 0))
            dp2[i] = max_reach
        
        ans, curr = 0, 0
        while curr < T:
            ans += 1
            curr = dp2[curr]
        return ans

