"""
https://leetcode.com/problems/sort-characters-by-frequency/

Count characters and their frequency. Sort, then build answer.
Time complexity: O(N), N = len(s).
Sort is O(52log52), since we have 52 different characters at most.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = {}
        for ch in s:
            if ch in cnt:
                cnt[ch] += 1
            else:
                cnt[ch] = 0
        cnt_list = [(-cnt[ch], ch) for ch in cnt]
        cnt_list.sort()
        ans = ''
        for n, ch in cnt_list:
            ans += ch * (-n)
        return ans
