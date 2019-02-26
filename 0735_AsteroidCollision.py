# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/asteroid-collision/

Put the asteroid in to a stack. Check the last two asteroids, if they collide, 
compute the result.

Time Complexity: O(n)
"""
class Solution:
    def asteroidCollision(self, asteroids):
        if len(asteroids) <= 1:
            return asteroids
        stack = []
        for n in asteroids:
            stack.append(n)
            while len(stack) >= 2 and stack[-1] < 0 < stack[-2]: #collision
                if abs(stack[-2]) > abs(stack[-1]): #last one explodes
                    stack.pop()
                elif abs(stack[-2]) == abs(stack[-1]): #both explode
                    stack.pop()
                    stack.pop()
                else: # the first one explodes
                    stack[-2], stack[-1] = stack[-1], stack[-2]
                    stack.pop()
        return stack

a = [10, 2, -5]
s = Solution()
print(s.asteroidCollision(a))
                
