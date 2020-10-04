"""
https://leetcode.com/problems/maximum-number-of-visible-points/

Compute all angles, sort it.

For each starting point with angle A, find the location to insert (A+angle), then we know the number of points can be seen.

Time complexity: O(NlogN)
"""
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles, n_duplicates = [], 0
        for p1, p2 in points:
            if p1 == location[0] and p2 == location[1]:
                n_duplicates += 1
            else:
                if p1 == location[0]: # 90 degree
                    if p2 > location[1]:
                        angles.append(math.pi/2)
                    else:
                        angles.append(-math.pi/2)
                else:
                    angles.append(math.atan2(p2 - location[1], p1 - location[0]))
        angles.sort()
        angles += [x + math.pi*2 for x in angles]
        ans = 0
        for i, a in enumerate(angles):
            idx = bisect.bisect_right(angles, a + angle/180*math.pi)
            ans = max(ans, n_duplicates + idx - i)
        return ans
