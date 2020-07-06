"""
https://leetcode.com/problems/plus-one/
Reverse the list, do add digit by digit.
Time Complexity: O(N)
"""
class Solution:
    def plusOne(self, digits):
        ans = digits[::-1]
        add_one = 1
        for i, d in enumerate(ans):
            if not add_one:
                break
            else:
                d += add_one
                if d >= 10:
                    d %= 10
                    add_one = 1
                else:
                    add_one = 0
                ans[i] = d
        if add_one:
            ans.append(1)
        return ans[::-1]
