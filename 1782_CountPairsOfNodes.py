"""
https://leetcode.com/problems/count-pairs-of-nodes/
"""
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cnt = [0] * (n+1)
        edge_cnt = {}
        for a, b in edges:
            cnt[a] += 1
            cnt[b] += 1
            if a > b:
                a, b = b, a
            edge_cnt[(a, b)] = edge_cnt.get((a, b), 0) + 1
        
        vals = sorted(cnt[1:])
        
        ans = []
        for q in queries:
            tmp = 0
            l, h = 0, n - 1
            while l < h:
                if q < vals[l] + vals[h]:
                    tmp += h - l
                    h -= 1
                else:
                    l += 1
            for u, v in edge_cnt:
                if cnt[u] + cnt[v] - edge_cnt[(u, v)] <= q < cnt[u] + cnt[v]:
                    tmp -= 1
            ans.append(tmp)
            
        return ans
                
                