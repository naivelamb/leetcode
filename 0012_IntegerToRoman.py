"""
https://leetcode.com/problems/integer-to-roman/

Roman numbers are consists of one, five and ten. 
For each digit, we need to check how to use one, five and ten to form it. 

Time complexity: O(N), N # of digit for num
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [['I', 'V', 'X'],
                 ['X', 'L', 'C'],
                 ['C', 'D', 'M'],
                 ['M', 'M', 'M']]
        
        ans, digit = '', 0
        while num:
            val = num % 10
            num = num // 10
            one, five, ten = roman[digit]
            if val <= 3:
                ans = one*val + ans
            elif val == 4:
                ans = one + five + ans
            elif val == 5:
                ans = five + ans
            elif val <= 8:
                ans = five + (val - 5) * one + ans
            elif val == 9:
                ans = one + ten + ans
            else:
                ans = ten + ans
            digit += 1
        return ans