"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
Sliding window of length len(p), record the count of characters in the window.
Time compelxity: O(n), n = len(s)
"""
class Solution:
    def findAnagrams(self, s: str, p: str):
        cnt, k = len(p), len(p)
        if cnt > len(s):
            return []

        ans = []
        ref = {}
        for ch in p:
            ref[ch] = ref.get(ch, 0) + 1

        for i in range(k):
            if s[i] in ref:
                ref[s[i]] -= 1
                if ref[s[i]] >= 0:
                    cnt -= 1

        if cnt == 0:
            ans.append(0)

        for i in range(1, len(s)-k+1):
            old_ch, new_ch = s[i-1], s[i+k-1]
            if old_ch in ref:
                ref[old_ch] += 1
                if ref[old_ch] > 0:
                    cnt += 1
            if new_ch in ref:
                ref[new_ch] -= 1
                if ref[new_ch] >= 0:
                    cnt -= 1
            if cnt == 0:
                ans.append(i)

        return ans
