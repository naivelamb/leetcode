"""
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

cnt[j] => prefix freq sum of s[:j]. We only have 26 characters, make cnt a 26 X n array. 
Then we check all possible substrings, find the beauty score.
Time complexity: O(n^2)
"""
class Solution:
    def beautySum(self, s: str) -> int:
        cnt = [[0] * 26 for _ in range(len(s) + 1)]
        for i, c in enumerate(s):
            i += 1
            if i > 0:
                cnt[i] = [x for x in cnt[i-1]]
            cnt[i][ord(c) - ord('a')] += 1
        
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                freq = [cnt[j][x] - cnt[i][x] for x in range(26)]
                tmp = []
                for x in freq:
                    if x > 0: tmp.append(x)
                ans += max(tmp) - min(tmp)
        return ans
        
        
        