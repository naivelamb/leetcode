"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Sliding window that covers head or tail. 

Time complexity: O(n)
"""
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ans = sum(cardPoints[n-k:])
        prev = ans
        for i in range(n-k+1, n+1):
            prev = prev - cardPoints[i-1] + cardPoints[(i+k-1)%n]
            ans = max(prev, ans)
        return ans