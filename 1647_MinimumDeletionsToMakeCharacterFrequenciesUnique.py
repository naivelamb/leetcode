"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

Get the frequencies, delete the most frequent elements to the next available frequency (one by one). Special treatment when deleted to 0. 

Time complexity: O(n), n = len(s). This is for get the frequency, the following steps are just O(26), which is O(1).
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1
        ref = collections.defaultdict(list)
        for k in cnt:
            ref[cnt[k]].append(k)
        
        vals = sorted(ref.keys())[::-1]
        ans = 0
        for v in vals:
            while len(ref[v]) != 1:
                c = ref[v].pop()
                tmp = v
                while tmp in ref and tmp > 0:
                    tmp -= 1
                ans += v - tmp
                ref[tmp].append(c)
        return ans