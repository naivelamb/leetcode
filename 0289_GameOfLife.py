"""
https://leetcode.com/problems/game-of-life/

Count # of living cells in neighbor. Then update.

Time complexity: O(mn)
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for a in range(max(0, i-1), min(m, i+2)):
                    for b in range(max(0, j-1), min(n, j+2)):
                        if (a, b) != (i, j) and board[a][b] in [1, 2]:
                            cnt += 1
                if board[i][j] == 0 and cnt == 3:
                    board[i][j] = 3
                if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                    board[i][j] = 2
        # update status
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1
        return 