"""
https://leetcode.com/problems/buddy-strings/
Record the indices of different letter. If more than 2 or only 1, return False.
If zero, we need to make sure at least one letter is duplicated.
If 2, we need to check whether we can swap to make them the same.

Time complexity: O(N)
"""
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        cnt = {}
        difference = []

        flag_duplicate = False
        for i in range(len(A)):
            cnt[A[i]] = cnt.get(A[i], 0) + 1
            if cnt[A[i]] > 1:
                flag_duplicate = True
            if A[i] != B[i]:
                difference.append([i, A[i], B[i]])

        if len(difference) > 2 or len(difference) == 1:
            return False
        elif len(difference) == 0:
            return flag_duplicate
        else:
            _, a1, b1 = difference[0]
            _, a2, b2 = difference[1]
            return (a1 == b2) & (b1 == a2)
