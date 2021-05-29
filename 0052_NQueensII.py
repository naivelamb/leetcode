"""
https://leetcode.com/problems/n-queens-ii/

backtracking. 
dfs(pos, n_queen) 
pos => position for n queen
n_queen => number of queens placed currently

need a helper function to check if the current placement is permited or not. 

Time complexity: O(n!)
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        def isValid(pos, n_queen):
            for i in range(n_queen):
                if abs(pos[i] - pos[n_queen]) == abs(i - n_queen) or pos[i] == pos[n_queen]:
                    return False
            return True
        

        self.ans = 0
        def dfs(pos, n_queen):
            if len(pos) == n_queen:
                self.ans += 1
                return
            
            for i in range(len(pos)):
                pos[n_queen] = i
                if isValid(pos, n_queen):
                    dfs(pos, n_queen + 1)

        pos = [-1] * n
        dfs(pos, 0)
        return self.ans