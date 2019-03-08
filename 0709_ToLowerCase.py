# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/to-lower-case/

Use order, chr transform
Time complexity: 
If using word += chr, it might be O(n^2) depends on the CPython version. 
It is suggested on wiki.python.org that best algorithms for string concatenation
is ''.join(seq), which is guarenteed to be O(n) 
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

    def toLowerCase_join(self, str: str) -> str:
        ans = []
        delta = ord('a') - ord('A')
        for ch in str:
            if ord('A') <= ord(ch) <= ord('Z'):#capital
                ans.append(chr(ord(ch) + delta))
            else:
                ans.append(ch)
        return ''.join(ans)
s = Solution()
a = 'Hello'
print(s.toLowerCase(a))