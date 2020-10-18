"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/

Record the position of each character, find the largest distance. 

Time complexity: O(N)
"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        ref = collections.defaultdict(list)
        for i, c in enumerate(s):
            ref[c].append(i)
            ans = max(ans, i - ref[c][0] - 1)
        return ans