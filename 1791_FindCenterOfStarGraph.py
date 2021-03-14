"""
https://leetcode.com/problems/find-center-of-star-graph/

Go through edges, count connected nodes for each node. 
Then go through node, find the one with (n - 1) edges. 

Time complexity: O(V + E)
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt, n = {}, 0
        for i, j in edges:
            cnt[i] = cnt.get(i, 0) + 1
            cnt[j] = cnt.get(j, 0) + 1
            n = max(n, i, j)
        
        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                return i