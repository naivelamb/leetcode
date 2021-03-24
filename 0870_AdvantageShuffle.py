"""
https://leetcode.com/problems/advantage-shuffle/

Greedy. Try to beat the smallest B with the smallest possible A. Store the "useless" A, random assign them to the unbeatable position. 

Time complexity: O(nlogn)

"""
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted([(x, i) for i, x in enumerate(B)])
        
        n = len(A)
        ans = [-1] * len(A)
        remaining = []

        i, j = 0, 0
        while i < n and j < n:
            if sortedB[j][0] < sortedA[i]:
                ans[sortedB[j][1]] = sortedA[i]
                i += 1
                j += 1
            else:
                remaining.append(sortedB[i])
                i += 1
        i = 0
        for k in range(n):
            if ans[k] == -1:
                ans[k] = remaining[i]
                i += 1

        return ans    