"""
https://leetcode.com/problems/truncate-sentence/
"""
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(' ')
        return ' '.join(s[:k])