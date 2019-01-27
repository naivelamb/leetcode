# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/string-without-aaa-or-bbb/

If A > B, we first build 'ab' * B pair, add one 'a' to the end, then start from
the begining, insert 'a' to make sure all 'a' is used.   
"""

class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == B:
            return 'ab' * A
        strs = ['a', 'b']
        # make sure A > B
        if A < B:
            A, B = B, A
            strs = ['b', 'a']
        
        ans = strs*B + strs[0:1]
        #remain As
        remain_A = A - B - 1
        i = 0
        while i < remain_A:
            ans[i*2] = strs[0]*2
            i += 1
        return ''.join(ans)

s = Solution()
print(s.strWithout3a3b(4, 1))
        