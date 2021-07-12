"""
https://leetcode.com/problems/find-median-from-data-stream/

Two heap, one for smaller part, one for larger part. 
When adding num, try to maitain the size of both part to be equal. To do this, we need to take the largest of smaller part and smallest of larger part out, sort them together with the new number, then put them back accordingly. When two parts are of same size, we put element into the larger part. 

time complexity: addNum: O(logN)
findMedian: O(N)
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller, self.larger = [], []
        self.total_len = 0

    def addNum(self, num: int) -> None:
        self.total_len += 1
        if not self.smaller and not self.larger:
            heapq.heappush(self.larger, num)
        elif not self.smaller:
            prev_val = heapq.heappop(self.larger)
            heapq.heappush(self.larger, max(prev_val, num))
            heapq.heappush(self.smaller, -min(prev_val, num))
        else:
            a = heapq.heappop(self.larger)
            b = -heapq.heappop(self.smaller)
            tmp = sorted([a, b, num])
            heapq.heappush(self.smaller, -tmp[0])
            heapq.heappush(self.larger, tmp[2])
            if len(self.smaller) < len(self.larger):
                heapq.heappush(self.smaller, -tmp[1])
            else:
                heapq.heappush(self.larger, tmp[1])

    def findMedian(self) -> float:
        if self.total_len % 2 == 0:
            return (self.larger[0] - self.smaller[0]) / 2
        else:
            return self.larger[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()