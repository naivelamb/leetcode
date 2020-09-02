"""
https://leetcode.com/problems/contains-duplicate-iii/

#1: Use Balanced Binary Search Tree to store the previous k elements. For everyone number, we need to find the min/max value in previous k element (O(logk)), then delete one element and include one element (O(1)), overall time complexity would be O(NlogK).

#2: Maintain buckets each of size (t+1) holding the last k elements.
When we come across with a number x, we can easily locate its corresponding bucket by looking at x//(t+1), then if there are numbers in the bucket, we return True. We also need to check the two neighbor buckets.

Each bucket would only contain 1 element, otherwise it means k > t, which guarentee we should return True.

Time Complexity: O(N)
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        cache = {}
        for i in range(len(nums)):
            if i - k > 0:
                bucket_id_to_delete = nums[i-k-1]//(t+1)
                del cache[bucket_id_to_delete]
            bucket_id = nums[i]//(t+1)
            condition1 = (bucket_id in cache)
            condition2 = (bucket_id+1 in cache and abs(cache[bucket_id+1] - nums[i]) <= t)
            condition3 = (bucket_id-1 in cache and abs(cache[bucket_id-1] - nums[i]) <= t)
            if condition1 or condition2 or condition3:
                return True
            cache[bucket_id] = nums[i]
        return False
