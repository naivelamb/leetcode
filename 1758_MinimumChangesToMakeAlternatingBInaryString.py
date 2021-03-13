"""
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
Let's assume the string should be '010101'
Check the number of character not correct ==> k
ans = min(k, n - k)

Time complexity: O(N)
"""
class Solution:
    def minOperations(self, s: str) -> int:
        ans = sum(i%2 == int(c) for i, c in enumerate(s))
        return min(ans, len(s) - ans)