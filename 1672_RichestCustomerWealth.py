"""
https://leetcode.com/problems/richest-customer-wealth/

Calculate each person's wealth. 
Time complexity: O(mn)
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for account in accounts:
            ans = max(ans, sum(account))
        return ans