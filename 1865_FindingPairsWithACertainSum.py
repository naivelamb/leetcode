"""
https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

len(nums1) << len(nums2)

In initialize, we store both counter and nums2 => O(M + N)
In add, update counter2 and nums2 => O(1)
In count, for all vals in nums1, try to find other pairs in nums2 => O(M)

"""
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        v0 = self.nums2[index]
        v1 = v0 + val
        self.cnt2[v0] -= 1
        self.cnt2[v1] += 1
        self.nums2[index] = v1

    def count(self, tot: int) -> int:
        ans = 0
        for k in self.cnt1:
            ans += self.cnt1[k] * self.cnt2.get(tot - k, 0)
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)