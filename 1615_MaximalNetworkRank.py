"""
https://leetcode.com/problems/maximal-network-rank/

Count the edges for all nodes, if two nodes are connected, then the rank would be (cnt_a + cnt_b - 1), else it is (cnt_a + cnt_b).

Time complexity: O(N^2)
"""
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        state = [[0] * n for _ in range(n)]
        for p1, p2 in roads:
            count[p1] += 1
            count[p2] += 1
            state[p1][p2] = 1
            state[p2][p1] = 1

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                val = count[i] + count[j]
                if state[i][j]:
                    val -= 1
                ans = max(ans, val)
        return ans
