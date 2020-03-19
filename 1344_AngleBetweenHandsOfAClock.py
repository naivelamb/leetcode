"""
https://leetcode.com/problems/angle-between-hands-of-a-clock/

Math problem, compute the positions of two hands, then get angle.
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        pos = minutes / 60
        pos_hour = (hour % 12) * 5 + 5 * pos
        angle = minutes *6 - pos_hour * 6
        if angle < 0:
            angle = - angle
        if angle > 180:
            angle = 360 - angle
        return angle
