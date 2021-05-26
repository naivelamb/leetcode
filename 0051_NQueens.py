"""
https://leetcode.com/problems/n-queens/

Try to place one queen at a time. Backtracking. 

To satisify the criteria, we need to make sure each row has only one queen. 
Use pos[i] to record the column of queen on i-th row. 
For any j != i, if pos[i] == pos[j] or abs(pos[i]- pos[j]) == abs(i - j), the two queen could kill each other. 
We need to build a helper function to check this. 

Then we use backtracking to find all possible queen placements. 
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []

        def isValid(pos, n_queen):
            for i in range(n_queen):
                if pos[i] == pos[n_queen] or abs(pos[n_queen] - pos[i]) == abs(n_queen - i):
                    return False
            return True

        def dfs(pos, n_queen, curr):
            if len(pos) == n_queen:
                self.res.append(curr)
                return
            
            for i in range(len(pos)):
                pos[n_queen] = i
                if isValid(pos, n_queen):
                    tmp = ['.'] * len(pos)
                    tmp[i] = 'Q'
                    tmp = ''.join(tmp)
                    dfs(pos, n_queen + 1, curr + [tmp])

        pos = [-1] * n 
        dfs(pos, 0, [])
        return self.res