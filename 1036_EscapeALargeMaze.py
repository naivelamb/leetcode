# -*- coding: utf-8 -*-:
"""
https://leetcode.com/problems/escape-a-large-maze/

If either one of the nodes is blocked, we cannont go from source to target. 
Need to determine the case if both points are in the same blocked region.

Since blocked.length <= 200, let's see what the largest possible covered area
1. Only use the blocks in the blocked => square, (50*sqrt(2))^2 = 5000
2. Use blocks and the boundary => triangle, (200*sqrt(2))^2/2 = 20000

Hence, we just need to go from source or target, BFS to expand untill we covered
an area 20000, if we can do so, then it is not covered.

Time complexity: O(40000)
"""
import collections
class Solution:
    def isEscapePossible(self, blocked, source, target):
        if not blocked:
            return True
        blocked = set((x, y) for x, y in blocked)
        
        def isBlocked(source, target, blocked):
            # determine if (r0, c0) is blocked or not
            r0, c0 = source
            r1, c1 = target
            queue = collections.deque([(r0, c0)])
            area = 0
            visited = {(r0, c0)}
            while queue:
                if area > 20000:
                    return False
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_x, new_y = x + dx, y + dy
                    if new_x == r1 and new_y == c1:# reach the other point
                        return False
                    if 0 <= new_x < 10**6 and 0 <= new_y < 10**6:
                        if (new_x, new_y) not in blocked and (new_x, new_y) not in visited:
                            area += 1
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y))
            return True
        
        if any([isBlocked(source, target, blocked), isBlocked(target, source, blocked)]):
            return False
        else:
            return True      
            