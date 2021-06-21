"""
https://leetcode.com/problems/shortest-distance-to-target-color/

Store the color in a hashmap. For each query, do binary search to find the place in the color.

Time complexity: O(K + NlogK), N = len(queries), K = len(colors)
"""
import bisect
class Solution:
    def shortestDistanceColor(self, colors, queries):
        ref = {}
        for i, c in enumerate(colors):
            if c in ref:
                ref[c].append(i)
            else:
                ref[c] = [i]

        memo = {}
        ans = []
        for idx, c in queries:
            if (idx, c) in memo:
                ans.append(memo[(idx, c)])
            else:
                if c in ref:
                    target = bisect.bisect_left(ref[c], idx)
                    if target == 0:
                        ans.append(abs(idx - ref[c][0]))
                    elif target >= len(ref[c]):
                        ans.append(abs(idx - ref[c][-1]))
                    else:
                        ans.append(min(abs(idx - ref[c][target-1]), abs(idx - ref[c][target])))
                else:
                    ans.append(-1)
                memo[(idx, c)] = ans[-1]

        return ans

    def shortestDistanceColor_dp(self, colors, queries):
        n = len(colors)
        distance = [[-1] * n for _ in range(3)]
        idxs = [-1, -1, -1]
        
        
        for i in range(n):
            color = colors[i] - 1
            idxs[color] = i
            for c in range(3):
                if idxs[c] == -1:
                    pass
                else:
                    distance[c][i] = i - idxs[c]
        
        idxs = [n, n, n]
        for i in range(n-1, -1, -1):
            color = colors[i] - 1
            idxs[color] = i
            for c in range(3):
                if idxs[c] == n:
                    pass
                else:
                    if distance[c][i] == -1:
                        distance[c][i] = idxs[c] - i
                    else:
                        distance[c][i] = min(distance[c][i], idxs[c] - i)
        
        ans = []
        for i, c in queries:
            ans.append(distance[c-1][i])
        return ans

sol = Solution()

colors = [1,1,2,1,3,2,2,3,3]
queries = [[1,3],[2,2],[6,1]]
assert sol.shortestDistanceColor_dp(colors, queries) == [3, 0, 3]

#colors = [1,2]
#queries = [[0,3]]
#assert sol.shortestDistanceColor(colors, queries) == [-1]
