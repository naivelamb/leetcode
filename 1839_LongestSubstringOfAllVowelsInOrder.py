"""
https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

2 pointers, maximum increasing order and count of characters. 

Time complexity: O(N)
"""
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        cnt = {word[0]: 1}
        l, r = 0, 1
        ans = 0
        while r < len(word):
            if word[r] >= word[r-1]:
                cnt[word[r]] = cnt.get(word[r], 0) + 1
            else: # break point, check 
                if cnt.get('a', 0) > 0 and cnt.get('e', 0) > 0 and cnt.get('i', 0) > 0 and cnt.get('o', 0) > 0 and cnt.get('u', 0) > 0:
                    ans = max(ans, r - l)
                cnt = {word[r]: 1}
                l = r
            r += 1
        if cnt.get('a', 0) > 0 and cnt.get('e', 0) > 0 and cnt.get('i', 0) > 0 and cnt.get('o', 0) > 0 and cnt.get('u', 0) > 0:
            ans = max(ans, r - l)
        return ans
                