"""
https://leetcode.com/problems/car-fleet-ii/

A car only collide with the car in front of it. 
We go from the end of the fleet, use a stack to maintain the index of car. We remove cars that will not collision with current car, or collision happend before. The collision of current car can be computed by comparing its position with the top element in the stack.

Time complexity: O(N)
"""
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        n = len(cars)
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            p, s = cars[i]
            while stack and (s <= cars[stack[-1]][1] or (p - cars[stack[-1]][0]) / (cars[stack[-1]][1] - s) >= ans[stack[-1]] > 0):
                stack.pop()
            if stack:
                ans[i] = (p - cars[stack[-1]][0])/(cars[stack[-1]][1] - s)
            stack.append(i)
        
        return ans
