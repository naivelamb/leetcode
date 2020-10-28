"""
https://leetcode.com/problems/minimum-number-of-frogs-croaking/

Store the count of 'croak', for every new letter, check whether 
cnt['c'] >= cnt['r'] >= cnt['o'] >= cnt['a'] >= cnt['k'] to make sure they are in seuqence. 

Number of forgs needed is max(cnt[c] for c in 'croak') - min(cnt[c] for c in 'croak').

At the end, check if cnt['c'] == cnt['r'] == cnt['o'] == cnt['a'] == cnt['k']

Time complexity: O(N)
"""
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = [0] * 5
        toIndex = {c: i for i, c in enumerate('croak')}

        count = 0
        for ch in croakOfFrogs:
            i = toIndex[ch]
            cnt[i] += 1
            if ch == 'c':
                count = max(count, cnt[0] - cnt[4])
                continue
            if cnt[i-1] < cnt[i]:
                return -1
        
        return count if cnt[0] == cnt[4] else -1