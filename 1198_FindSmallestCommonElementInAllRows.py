"""
https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

1). Brute force: O(n^3)
2). For each element in row[0], search its existence in the other rows, O(n^2log(n))
3). If there is no duplicate elements in each row, the common elements must appear m times.
    Hence we can go over all the elment, count the frequence, find those element that appears m times.
    Then find the smallest one. Time complexity: O(mn)
"""
class Solution:
    def smallestCommonElement(self, mat):
        m, n = len(mat), len(mat[0])
        freq = {}

        for i in range(m):
            for j in range(n):
                if mat[i][j] in freq:
                    freq[mat[i][j]] += 1
                else:
                    freq[mat[i][j]] = 1
                if mat[i][j] == m:
                    return mat[i][j]
        return -1


sol = Solution()

mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
assert sol.smallestCommonElement(mat) == 5
