"""
https://leetcode.com/problems/online-majority-element-in-subarray/

Since the element is a majority element, we random pick one element, we have 50% chance of picking the desired element.

If we do the picking for 10 times, our chance of missing it is 1/2^10.

So we store the indices of the element. We random pick an element from the subarray, then do binary search to find the left and right in the indices array, next check whether its occurance exceed threshold.

So time complexity is O(10logN)
"""

class MajorityChecker:

    def __init__(self, arr):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(arr):
            a2i[x].append(i)
        self.A, self.a2i = arr, a2i

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(10):
            a = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
