# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Sliding window, use hashmap to record the count of characters in the window
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k == 0:
            return 0
        cnt = {}
        ans, l, r = 0, 0, 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            while len(cnt) > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
    
s = Solution()
a = 'eceba'
print(s.lengthOfLongestSubstringKDistinct(a, 2))
a = 'aa'
print(s.lengthOfLongestSubstringKDistinct(a, 1))
