"""
https://leetcode.com/problems/filling-bookcase-shelves/
dp[i] -> answer for books[:i]

for dp[i], we need to look back to j, such that,
sum(book[j:i][0] <= shelf_width)
for each book j, dp[i] = dp[j] + max_height, where max_height = max(book[j:i][1])

Time complexity: O(n^2)
"""
class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[n]

sol = Solution()

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
assert sol.minHeightShelves(books, 4) == 6
