"""
https://leetcode.com/problems/word-break-ii/

DFS + backtracking.
if prefix = s[0:k], then the answer is
prefix + wordBreak(s[k:], wordDict).
This build the recursion.

We need a memo to store the results for using i as start idx to avoid duplication.

Time compelxity: O(N*2^N), N = len(s)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        def dfs(start_idx):
            if start_idx == len(s):
                return [""]
            if start_idx in memo:
                return memo[start_idx]

            res = []
            for j in range(start_idx, len(s)):
                prefix = s[start_idx: j+1]
                if prefix in wordDict:
                    rem = dfs(j+1)
                    for word in rem:
                        new_word = prefix + ' ' + word
                        res.append(new_word.strip())

            memo[start_idx] = res
            return res

        return dfs(0)
