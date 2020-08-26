"""
https://leetcode.com/problems/fizz-buzz/
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0:
                if i % 3 == 0 and i % 5 == 0:
                    ans.append('FizzBuzz')
                elif i % 3 == 0:
                    ans.append('Fizz')
                else:
                    ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans
