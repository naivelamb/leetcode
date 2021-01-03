"""
https://leetcode.com/problems/beautiful-arrangement/

a_i % i == 0
i % a_i == 0

Try all permutations 
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        self.cnt = 0
        visited = [0] * (n + 1)
        def helper(n, pos, visited):
            if pos > n:
                self.cnt += 1
            for i in range(1, n+1):
                if (visited[i] == 0) & ((pos % i == 0) | (i % pos == 0)):
                    visited[i] = 1
                    helper(n, pos + 1, visited)
                    visited[i] = 0
        helper(n, 1, visited)
        return self.cnt    