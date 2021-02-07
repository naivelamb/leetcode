"""
https://leetcode.com/problems/shortest-distance-to-a-character/

Go from left to right, record distance. 
Then go from right to left, find the minimum distance. 

Time complexity: O(N)
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i, x in enumerate(s):
            if x == c: prev = i
            ans.append(i - prev)
        
        prev = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c: prev = i
            ans[i] = min(ans[i], prev - i)
        return ans