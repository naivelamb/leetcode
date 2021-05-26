"""
https://leetcode.com/problems/find-the-shortest-superstring/

Since no word in words is substring of another word, when forming string of two words, we can only put one after the other. 
So we need to build a helper dp, where
dp[i][j] means the maximum length of shared parts of words[i] and words[j] if we form them in the order of
word[i], word[j]

Then we need to check all possibility of forming strings. 
here we need to use another dp array
dp[mask][k] means to form “mask" string by adding words[k] at the end, the shortest supersting. 

mask = 2 ^ n, max(k) = n

Time complexity: O(2^n * n^2)

"""
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        shared = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(min(len(words[i]), len(words[j])), -1, -1):
                    if words[i][-k:] == words[j][:k]:
                        shared[i][j] = k
                        break
        
        dp = [[''] * 12 for _ in range(1 << 12)]
        for i in range(1 << n):
            for k in range(n):
                if not (i & (1 << k)):
                    # impossible since mask does not contain k
                    continue
                if i == 1 << k:
                    # k is the starting node
                    dp[i][k] = words[k]
                    continue
                for j in range(n):
                    # check all possible previous node j 
                    if j == k:
                        continue
                    if i & (1 << j):
                        s = dp[i ^ (1 << k)][j]
                        s += words[k][shared[j][k]:]
                        if dp[i][k] == '' or len(s) < len(dp[i][k]):
                            dp[i][k] = s
        
        min_len = float('inf')
        res = ''
        for i in range(n):
            s = dp[(1 << n) - 1][i]
            if len(s) < min_len:
                res, min_len = s, len(s)

        return res