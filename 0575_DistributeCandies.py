"""
https://leetcode.com/problems/distribute-candies/

min(len(set(candyType)), len(candyType)//2)

Time complexity: O(N)
"""
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)