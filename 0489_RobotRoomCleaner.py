# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/robot-room-cleaner/

Clearly a DFS problem. The key is how to move back to previous location. 

Initial direction is (0, 1) -- turn left --> (-1, 0) -- turn left --> (0, -1) 
-- turn left --> (1, 0)

Think about the edge case, when we enter a position that is a dead end, we want 
to get back to previous position and turn to previous direction. 
When the robot realizes it reaches a dead end, it has turned left 4 times. To 
turn to the opposite direction, we need to turn left for 2 more times, then 
move (get back). Now turn left two more times, we are facing the previous 
direction. 

"""

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        def dfs(x, y, dx, dy):
            # clean 
            robot.clean()
            visited.add((x, y))
            
            # try to clean neighbor spots
            for _ in range(4):
                if (x + dx, y + dy) not in visited and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                robot.turnLeft()
                dx, dy = -dy, dx
            
            # get back
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        dfs(0, 0, 0, 1)
            