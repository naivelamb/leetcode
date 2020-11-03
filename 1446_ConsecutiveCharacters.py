"""
https://leetcode.com/problems/consecutive-characters/

Record current length of same characters.

Time complexity: O(N)
"""
class Solution:
    def maxPower(self, s: str) -> int:
        ans, curr = 1, 1
        prev = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                curr += 1
            else:
                prev = s[i]
                curr = 1
            ans = max(ans, curr)
        return ans