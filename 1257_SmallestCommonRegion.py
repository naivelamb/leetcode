"""
https://leetcode.com/problems/smallest-common-region/

Build the relation in a tree. Find the Lowest Common Ancestor.
Time complexity: O(N)
"""

class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        parents = {region[i]: region[0] for region in regions for i in range(1, len(region))}
        ancestery_history = {region1}
        while region1 in parents:
            region1 = parents[region1]
            ancestery_history.add(region1)
        while region2 not in ancestery_history:
            region2 = parents[region2]
        return region2

sol = Solution()
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]]
region1 = "Quebec"
region2 = "New York"
assert sol.findSmallestRegion(regions, region1, region2) == 'North America'
