"""
https://leetcode.com/problems/finding-mk-average/

Maintain a sorted array of length m. 

Time complexity:
addElement: O(M)
calculateMKAverage: O(M)
"""
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.vals = []
        self.sorted_vals = []
        self.n = 0
        

    def addElement(self, num: int) -> None:
        self.vals.append(num)
        bisect.insort(self.sorted_vals, num)
        self.n += 1
        if self.n > self.m:
            v = self.vals[self.n - self.m - 1]
            self.sorted_vals.remove(v)
        
    def calculateMKAverage(self) -> int:
        if self.n  < self.m:
            return -1
        return int(sum(self.sorted_vals[self.k: self.m-self.k])/(self.m - 2*self.k))