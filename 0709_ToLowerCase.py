# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/to-lower-case/

Use order, chr transform
Time complexity: O(n)
"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ''
        delta = ord('a') - ord('A')
        for ch in str:
            if ord('A') <= ord(ch) <= ord('Z'):#capital
                ans += chr(ord(ch) + delta)
            else:
                ans += ch
        return ans
    
s = Solution()
a = 'Hello'
print(s.toLowerCase(a))