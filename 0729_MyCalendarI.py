"""
https://leetcode.com/problems/my-calendar-i/

Store calendar as a sorted list. Check if a new book can be added. 

Time complexity: O(logN + N)
"""
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
         i = bisect.bisect_right(self.calendar, start)
         j = bisect.bisect_left(self.calendar, end)
         
         if i % 2: return False
         if i != j: return False
         self.intervals[i:i] = [start, end]
         return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)