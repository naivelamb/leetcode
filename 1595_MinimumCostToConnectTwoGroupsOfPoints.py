"""
We use mask to record which elemetns in group 2 has been connected.
dp[i][mask] represent the minimum cost for connect the first-i nodes in group 1 to some nodes in group 2, which is recorded using the mask.

At the end, we connect the unconnected nodes in group 2 using the cheapest cost.

Time Complexity: O(mn * 2^m). m -> # of nodes in group 1; n -> # of nodes in group 2.
"""
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        sz1, sz2 = len(cost), len(cost[0])
        min_sz2 = [min([cost[i][j] for i in range(sz1)]) for j in range(sz2)]

        @lru_cache(None)
        def dfs(i: int, mask:int):
            res = 0 if i >= sz1 else float('inf')
            if i >= sz1:
                for j in range(sz2):
                    if mask & (1 << j) == 0:
                        res += min_sz2[j]
            else:
                for j in range(sz2):
                    res = min(res, cost[i][j] + dfs(i+1, mask | (1 << j)))
            return res

        return dfs(0, 0)
