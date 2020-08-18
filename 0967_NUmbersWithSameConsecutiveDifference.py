"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Give a node with val, the children nodes would be (val + k) and (val - k), as long as both values are in the range [0, 9].

Use dfs to build the tree and traversal it.

Time Complexity: O(N*2^N)
"""
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = []
        if N == 1:
            return [x for x in range(10)]
        if K == 0:
            return [int(str(x) * N) for x in range(1, 10)]

        def dfs(curr, N, K):
            if len(curr) == N:
                ans.append(int(curr))
                return
            last_num = int(curr[-1])
            n1 = last_num + K
            n2 = last_num - K
            if 0 <= n1 <= 9:
                dfs(curr + str(n1), N, K)
            if 0 <= n2 <= 9:
                dfs(curr + str(n2), N, K)

        for i in range(1, 10):
            dfs(str(i), N, K)
        return ans
