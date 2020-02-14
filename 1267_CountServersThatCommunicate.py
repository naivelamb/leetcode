"""
https://leetcode.com/problems/count-servers-that-communicate/

First build dictionary to record the number of computers in each row and col.
Then we loop over the grid again, if either the row or the col has >= 2 computers, we add it to answer

Time complexity: O(mn)
"""
class Solution:
    def countServers(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1:
                        ans += 1
                    elif cols[j] > 1:
                        ans += 1
        return ans

sol = Solution()
assert sol.countServers([[1,0],[1,1]]) == 3
assert sol.countServers([[1,0],[0,1]]) == 0
assert sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4
