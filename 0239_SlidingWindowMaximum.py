"""
https://leetcode.com/problems/sliding-window-maximum/

PQ. Use seen to record count of num. If PQ element count is 0, pop and go next.
Time complexity: O(NlogK)

DQ. 
Use DQ to maintain the largest element we've seen. It also records the numbers after the "maximum" element, aka next best candidates. 
When a new element comes, we check:
1). If DQ[0] is pointing to the correct range. 
2). If the number DQ[0] pointed is larger than the current num. 
3). Check from the tail to see if the current num is the new next best candidate. 
Each number will be visited twice. 
Time complexity: O(N)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 0:
            return nums
        
        dq = collections.deque()
        result = []

        for i in range(k):
            while len(dq) != 0:
                if nums[i] > nums[dq[-1]]:
                    dq.pop()
                else:
                    break
            dq.append(i)
        
        for i in range(k, len(nums)):
            result.append(nums[dq[0]])

            if dq[0] < i - k + 1:
                dq.popleft()
            
            while len(dq) != 0:
                if nums[i] > nums[dq[-1]]:
                    dq.pop()
                else:
                    break
            dq.append(i)
        
        result.append(nums[dq[0]])
        return result