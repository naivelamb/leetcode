"""
https://leetcode.com/problems/palindrome-partitioning/

Use dfs. 

dfs(s, path, res)
s: current string
path: current splitting result. 
res: record final results

Time complexity: O(N * 2^N), N = len(s)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res
    

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]