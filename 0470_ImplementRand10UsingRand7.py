"""
https://leetcode.com/problems/implement-rand10-using-rand7/
"""
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        ans = 0
        for i in range(10):
            ans += rand7()
        return (an % 10) + 1
