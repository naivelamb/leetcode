# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/bulls-and-cows/

Count of A: a, count of B: b.
Scan both secret and guess:
If match, a += 1
Else, put the number from secret into cnt1, the number from guess to cnt2. 

Then compare the count in cnt1 and cnt2 to get b.
b = sum(min(cnt1[key], cnt2.get(key, 0)) for key in cnt1)
"""
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = 0
        cnt1, cnt2 = {}, {}
        for i in range(len(secret)):
            c1, c2 = secret[i], guess[i]
            if c1 == c2:
                a += 1
            else:
                cnt1[c1] = cnt1.get(c1, 0) + 1
                cnt2[c2] = cnt2.get(c2, 0) + 1
        b = sum([min(cnt1[key], cnt2.get(key, 0)) for key in cnt1])
        return '{}A{}B'.format(a, b)

s = Solution()
secret = "1807"
guess = "7810"
print('Expected is 1A3B, get: ', s.getHint(secret, guess))
secret = "1123"
guess = "0111"
print('Expected is 1A1B, get: ', s.getHint(secret, guess))