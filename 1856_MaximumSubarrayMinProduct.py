"""
https://leetcode.com/problems/maximum-subarray-min-product/

For each nums[i], find next smaller element in the left and in the right, the answer is
sum(nums[l:r]) * nums[i]

Time complexity: O(N)
"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        p_sum = [0]
        for i, x in enumerate(nums):
            p_sum.append(p_sum[-1] + x)
        # next smaller element in the right
        cache, st = {}, []
        for i, x in enumerate(nums):
            if len(st) == 0:
                st.append((i, x))
            elif x >= st[-1][1]:
                st.append((i, x))
            else:
                while st and st[-1][1] > x:
                    cache[st.pop()[0]] = i
                st.append((i, x))
        # next smaller element in the left        
        cache2, st = {}, []
        for i, x in enumerate(nums[::-1]):
            if len(st) == 0:
                st.append((i, x))
            elif x >= st[-1][1]:
                st.append((i, x))
            else:
                while st and st[-1][1] > x:
                    cache2[st.pop()[0]] = i
                st.append((i, x))
                
        ans = 0
        n = len(nums)
        for k, x in enumerate(nums):
            j = cache.get(k, n)
            i = n - cache2.get(n-1-k, n)
            #print(i, j, k)
            ans = max(ans, x * (p_sum[j] - p_sum[i]))
        return ans % (10**9 + 7)