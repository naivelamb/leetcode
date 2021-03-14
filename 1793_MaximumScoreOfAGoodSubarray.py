"""
https://leetcode.com/problems/maximum-score-of-a-good-subarray/submissions/

Brute Force.
Build dp, where dp[i][j] is min(nums[i:j]). Then go through dp. 
Time complexity: O(n^2), n = len(nums)

Greedy + Two pointer
Start from k, try to expand the interval. Always try to expand to the larger one first.
Time complexity: O(N)
"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.insert(0, -1)
        nums.append(-1)

        k += 1

        left, right = k, k
        mi = nums[k]
        cnt = 1
        score = mi * cnt

        max_score = score
        while nums[left - 1] > 0 or nums[right + 1] > 0:
            left_val = nums[left - 1]
            right_val = nums[right + 1]
            if right_val > left_val:
                right += 1
                mi = min(mi, right_val)
                cnt += 1
                score = mi * cnt
            else:
                left -= 1
                mi = min(mi, left_val)
                cnt += 1
                score = mi * cnt
            max_score = max(max_score, score)
        return max_score