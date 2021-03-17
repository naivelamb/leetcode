"""
https://leetcode.com/problems/merge-strings-alternately/

pointer. 
Time complexity: O(m + n)
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, ans = 0, ''
        while i < len(word1) and i < len(word2):
            ans += word1[i] + word2[i]
            i += 1
        return ans + word1[i:] + word2[i:]