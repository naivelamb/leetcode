"""
https://leetcode.com/problems/tree-of-coprimes/

Notice that, nums[i] in [1, 50], len(nums) in [1, 10^5], so we can iterate all possible nums[i].

When DFS, the path we go through contains all the ancestor. So we store all the possible numbers and their depth. When meeting a node, we check all possible numbers, and find its nearest coprime ancestor. 

So we do DFS + backtracking. 

Time complexity: O(50n)
"""
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        # build graph
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        ans = [-1] * n
        path = [[] for _ in range(51)]
        seen = set()
        
        def dfs(node, depth):
            if node in seen: return
            
            seen.add(node)
            largestDepth = -1
            for x in range(1, 51): #check all possible values
                if gcd(nums[node], x) == 1: # coprime
                    if len(path[x]) > 0: # has ancestor
                        topNode, topDepth = path[x][-1]
                        if largestDepth < topDepth:
                            largestDepth = topDepth
                            ans[node] = topNode
            path[nums[node]].append((node, depth))
            for nei in graph[node]:
                dfs(nei, depth + 1)
            path[nums[node]].pop()

        dfs(0, 0)
        return ans

        return ans