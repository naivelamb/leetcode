"""
https://leetcode.com/problems/course-schedule-iii/

We always try to finish the course with earlier deadline. And there is no harm to take courses that end earlier. 

If we cannot make the current course, we try to unlearn previous longest course.

Time complexity: O(nlogn)
"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        que, cur = [], 0
        for t, d in courses:
            heapq.heappush(que, -t)
            cur += t
            if cur > d:
                cur += heapq.heappop(que)
        return len(que)