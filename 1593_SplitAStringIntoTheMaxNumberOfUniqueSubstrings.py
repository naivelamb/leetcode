"""
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

Backtracking
Time Complexity: O(2^N)
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(s, seen):
            ans = 0
            if s:
                for i in range(1, len(s) + 1):
                    cand = s[:i]
                    if cand not in seen:
                        seen.add(cand)
                        ans = max(ans, 1 + helper(s[i:], seen))
                        seen.remove(cand)
            return ans

        return helper(s, set())
