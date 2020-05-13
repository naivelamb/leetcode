"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""
class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates) == 2:
            return True
        if coordinates[0][0] == coordinates[1][0]:
            for c in coordinates[2:]:
                if c[1] != coordinates[0][1]:
                    return False
        else:
            a, b = coordinates[0], coordinates[1]
            for c in coordinates[2:]:
                if (c[1] - b[1]) != (a[1] - b[1]) / (a[0] - b[0]) *  (c[0] - b[0]):
                    return False
        return True

sol = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
assert sol.checkStraightLine(coordinates) == True
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
assert sol.checkStraightLine(coordinates) == False
