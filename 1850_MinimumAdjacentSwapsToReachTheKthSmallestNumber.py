"""
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

Brute force. First find next kth permutation, then find minimum swaps. 
"""
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def nxt_perm(num: list) -> list:
            i = n - 1
            while i > 0 and num[i-1] >= num[i]:
                i -= 1
            j = i
            while j < n and num[i-1] < num[j]:
                j += 1
            num[i-1], num[j-1] = num[j-1], num[i-1]
            num[i:] = sorted(num[i:])
            return num

        n = len(num)
        nxt_k_num = list(num)
        for _ in range(k):
            nxt_k_num = nxt_perm(nxt_k_num)

        ans = 0
        num = list(num)
        for i in range(n):
            j = i
            while j < n and nxt_k_num[i] != num[j]:
                j += 1
            ans += j - i
            num[i:j+1] = [num[j]] + num[i:j]
        return ans        