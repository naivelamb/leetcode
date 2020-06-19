"""
https://leetcode.com/problems/longest-duplicate-substring/
Use binary search to find the length. For a given length, use Rabin-Karp to find whether there are duplicate substrings.

Time Complexity: O(NlogN), N=len(S)
"""
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y)%mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i-L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)

        res, l, r = 0, 0, len(S)
        while l < r:
            mid = (l + r + 1) // 2
            pos = test(mid)
            if pos:
                l = mid
                res = pos
            else:
                r = mid - 1
        return S[res: res + l]
