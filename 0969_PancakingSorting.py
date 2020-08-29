"""
https://leetcode.com/problems/pancake-sorting/

Find the max element's index: m_i, do the flip:
A[:m_i+1], then flip the unsorted part.
Keep doing this.

Complexity: O(N^2)
"""
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def findmax(A, current_size):
            idx = 0
            for i in range(current_size):
                if A[i] >= A[idx]:
                    idx = i
            return idx

        curr_size = len(A)
        ans = []
        while curr_size > 1:
            m_i = findmax(A, curr_size)
            if m_i != curr_size - 1:
                ans.append(m_i + 1)
                A = A[:m_i+1][::-1] + A[m_i+1:]
                ans.append(curr_size)
                A = A[:curr_size][::-1] + A[curr_size:]
            curr_size -= 1
        return ans
