"""
https://leetcode.com/problems/monotone-increasing-digits/
Build digit by digit.

"""
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = []
        A = list(map(int, str(N)))
        for i in range(len(A)):
            for d in range(1, 10):
                if digits + [d] * (len(A) - i) > A:
                    digits.append(d-1)
                    break
            else:
                digits.append(9)
        return int("".join(map(str, digits))) 
