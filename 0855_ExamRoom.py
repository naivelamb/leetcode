# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/exam-room/

#1 Naive Solution
Maintain a sorted list of seated student. 
The maximum position can be computed by one scan. 
Remove is just list.remove(p). 
Time Complexity: Both are O(n)
"""
import bisect
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = [] #students that seat. 

    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    if (s - prev) // 2 > dist:
                        dist, student = (s - prev) // 2, (s + prev) // 2
            if self.N - 1 - self.students[-1] > dist:
                dist, student = self.N - 1 - self.students[-1], self.N - 1
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)
