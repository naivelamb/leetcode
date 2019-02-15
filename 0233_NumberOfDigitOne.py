# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/number-of-digit-one/

Let's say f(n) gives the number of digit one for all number <= n.
Then we know:
f(9) = 1
For 99,  we have x1 => 10 * f(9) and 1x => 10, so,
f(99) = f(9) * 10 + 10
For 999, we have x99 and 1xx, so
f(999) = f(99) * 10 + 100
Based on this we can first build the reference for all '999' smaller than n. 
Then let's check what should we do about a normal number n. 

Take 23 as an example, 
23 = [0, 9] + [10, 19] + [20, 23] = 2*f(9) + 10 + f(3)

Then take 2458 as an example, 
f(2458) += (2458 // 1000) * f(1000 - 1)
f(2458) += (2458//1000 > 1 ? 1000: 0)
f(2458) += (2458//1000 == 1? 458 + 1: 0)
f(2458) += f(458)

"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {9: 1}
        num, i = 9, 1
        while 9 + num*10 <= n:
            memo[9 + num*10] = 10 * memo[num] + 10**i
            num = 9 + num*10
            i += 1
        
        def helper(n):
            if n <= 0: return 0
            if n <= 9: return 1
            ans = 0
            divisor = 10**(len(str(n)) - 1)
            n1 = n // divisor
            ans += n1 * memo[divisor - 1]
            if n1 > 1:
                ans += divisor
            if n1 == 1:
                ans += n % divisor + 1
            ans += helper(n % divisor)
            return ans
        
        return helper(n)
    
s = Solution()
print('Expected: 301, get: ', s.countDigitOne(1000))