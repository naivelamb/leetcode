"""
https://leetcode.com/problems/jewels-and-stones/

Convert J to a set. O(m)
Check each stone in S. O(n)
Time complexity: O(m + n), m = len(J), n = len(S)
"""
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(list(J))
        ans = 0
        for ch in S:
            if ch in J:
                ans += 1
        return ans

sol = Solution()
assert sol.numJewelsInStones("aA", "aAAbbbb") == 3
assert sol.numJewelsInStones("z", "ZZ") == 0
