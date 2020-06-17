"""
https://leetcode.com/problems/surrounded-regions/

Find the boundary "O", mark all positions connected to boundary "O", make the rest "O" as "X".

Time complexity: O(mn), (m, n) = size(board)
"""
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        m, n = len(board), len(board[0])
        # find starting points
        stack = []
        for i in range(m):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][n-1] == "O":
                stack.append((i, n-1))
        for j in range(n):
            if board[0][j] == "O":
                stack.append((0, j))
            if board[m-1][j] == "O":
                stack.append((m-1, j))
        # find positions connected to boundary
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "S"
                stack += [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        # flip positions
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
