"""
https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

Sliding window to record the frequence of characters.
Time complexity: O(NK)
"""
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n = len(S)
        if n < K:
            return 0
        if K > 26:
            return 0
        count = 0
        for i in range(n-K+1):
            if len(S[i:i+K]) == len(set(S[i:i+K])):
                count += 1
        return count
