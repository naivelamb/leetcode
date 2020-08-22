"""
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

We can randomly choose a rectangle and then randomly pick a point. This does not guarentee all points are uniformly and randomly picked, since rectangles have different areas. Therefore we need to assign weights to the rectangles.

The idea is build a prefix sum array for the rectangles area. When pick point, first generate a random number, binary search in the prefix_sum array to locate the index of rectangle, then randomly pick up a point in the rectangle.

Time complexity:
__init__(): O(N)
pick(): O(logN)
N = len(rectangles) 
"""
class Solution:

    def __init__(self, rects: List[List[int]]):
        w = [(x2 - x1 + 1) * (y2 - y1 + 1) for (x1, y1, x2, y2) in rects]
        self.weights = [w[0]]
        for i in range(1, len(w)):
            self.weights.append(self.weights[-1] + w[i])
        total = sum(w)
        self.weights = [x/total for x in self.weights]
        self.rects = rects

    def pick(self) -> List[int]:
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
