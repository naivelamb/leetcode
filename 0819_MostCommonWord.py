# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/most-common-word/

Use dictionary to keep count

Time complexity: O(n)
"""
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        data = re.split('\W+', paragraph)
        banned = set(banned)
        cnt, most, ans = {}, 0, ''
        for word in data:
            word = word.lower()
            if word in banned:
                continue
            else:
                cnt[word] = cnt.get(word, 0) + 1
                if cnt[word] > most:
                    most = cnt[word]
                    ans = word
        return ans

s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
print(s.mostCommonWord(paragraph, ['hit']))
        
