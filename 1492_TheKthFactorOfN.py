"""
https://leetcode.com/problems/the-kth-factor-of-n/

Brute force
Check all v in range [1, n], find the kth values. 
Time complexity: O(n)


"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        return 1