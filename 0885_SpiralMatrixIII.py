"""
https://leetcode.com/problems/spiral-matrix-iii/

Directions order are: (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
The pace we move are 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6.
We can think about an imaginary 'big' board to handle the out of bound situation, we walk through the spot but do not record them. 

Use dfs to do the traverse.

Time complexity: O(max(R, C)^2)

"""
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        if R == C == 0:
            return []
        ans = [[r0, c0]]

        def spiralTraverse(r, c, dr, dc, pace, ans):
            for _ in range(pace):
                r, c = r + dr, c + dc
                if 0 <= r < R and 0 <= c < C:
                    ans.append([r, c])
            next_dr, next_dc = dc, -dr #(0, 1) -> (1, 0) -> (0, -1) ->  (-1， 0)
            if next_dr == 0: #we are turning left/right, pace + 1
                next_pace = pace + 1
            else:
                next_pace = pace
            if len(ans) == R*C:
                return
            spiralTraverse(r, c, next_dr, next_dc, next_pace, ans)

        spiralTraverse(r0, c0, 0, 1, 1, ans)
        return ans

sol = Solution()

R = 1
C = 4
r0 = 0
c0 = 0
assert sol.spiralMatrixIII(R, C, r0, c0) == [[0,0], [0,1], [0,2], [0,3]]

R = 5
C = 6
r0 = 1
c0 = 4
assert sol.spiralMatrixIII(R, C, r0, c0) == [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
