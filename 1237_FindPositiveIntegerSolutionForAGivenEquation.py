"""
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

For a given X, binary search Y
Time complexity: O(XlogY).
"""

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans, f = [], customfunction.f
        for x in range(1, 1001):
            if f(x, 1) > z or f(x, 1000) < z: continue
            l, r = 1, 1000
            while l < r:
                y = (l + r) // 2
                if f(x, y) < z:
                    l = y + 1
                elif f(x, y) == z:
                    ans.append([x, y])
                    break
                else:
                    r = y
        return ans

     def findSolution_linear(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        y = 1000
        for x in range(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                ans.append([x, y])
        return ans       