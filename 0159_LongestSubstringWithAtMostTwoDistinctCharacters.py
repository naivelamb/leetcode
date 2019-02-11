# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Sliding window, use hashmap to record the count of characters in the window
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 2: return n
        cnt = {}
        l, r, ans = 0, 0, 0
        for r in range(n):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            while len(cnt) > 2:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans

s = Solution()
a = 'eceba'
print(s.lengthOfLongestSubstringTwoDistinct(a))
