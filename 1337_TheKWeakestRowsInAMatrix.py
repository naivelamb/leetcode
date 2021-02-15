"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
Go through the matrix to record (i, n) pair, which means the i-th row has n soliders.
We can do binary search to count solider faster 
Store all the (i, n) pair in a heap, then pop first k element.

Time complexity: O(mlogn + klogm)
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ref = []
        for i, row in enumerate(mat):
            if row[0] == 0:
                ref.append((0, i))
            elif row[-1] == 1:
                ref.append((len(row), i))
            else:
                l, r = 0, len(row)
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] == 1:
                        if mid + 1 == len(row) or row[mid + 1] == 0:
                            break
                        else:
                            l = mid
                    else:
                        r = mid
                ref.append((mid + 1, i))

        heapq.heapify(ref)
        ans = []
        while k:
            ans.append(heapq.heappop(ref)[1])
            k -= 1
        return ans