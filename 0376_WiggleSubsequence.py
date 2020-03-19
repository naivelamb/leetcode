"""
https://leetcode.com/problems/wiggle-subsequence/

1). Two dp array.
up[i] -> max length ending with nums[i] and wiggle up.
down[i] -> max length ending with nums[i] and wiggle down.

For a nums[i], to get up[i] and down[i] we need to check all 0 <= j < i.

Time complexity: O(n^2), n = len(nums)

2). We don't need to check every j < i.
up[i] -> max length for nums[:i+1], last one wiggle up.
down[i] -> max length for nums[:i+1], last one wiggle down.

If nums[i] > nums[i-1]
a. nums[i-1] is the last element of down[i-1] sub sequence, then up[i] = down[i-1] + 1
b. nums[i-1] is not the last element of down[i-1] sub sequence. That means nums[i] > k, where k is the last element of the down[i-1] sub sequence. Hence, we can still add nums[i] to the subsequence to build a longer wiggle up sequence. up[i] = down[i-1] + 1

No matter what, down[i] = down[i-1]

For nums[i] < nums[i-1], just flip up/down dp array around.
For nums[i] == nums[i-1], up[i] = up[i-1], down[i] = down[i-1].

Time complexity: O(n), n = len(nums)
"""
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        up, down = [1] * n, [1] * n
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i-1] < nums[i]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1], down[-1])

    def wiggleMaxLength_n2(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        up, down = [1] * n, [1] * n
        ans = 1
        for i in range(1, n):
            j = i - 1
            while j >= 0:
                if nums[j] > nums[i]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[j] < nums[i]:
                    down[i] = max(down[i], up[j] + 1)
                j -= 1
            ans = max(up[i], down[i])
        return ans

sol = Solution()
assert sol.wiggleMaxLength([1,7,4,9,2,5]) == 6
assert sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7
assert sol.wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2
