"""
https://leetcode.com/problems/largest-merge-of-two-strings/
Greedy. 

If word1[i:] > word2[j:], merge += word1[i]
Else merge += word2[j]

Time complexity: O(mn)
"""
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j, merge = 0, 0, ''
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                merge += word1[i]
                i += 1
            else:
                merge += word2[j]
                j += 1
        merge += word1[i:] + word2[j:]
        return merge
                