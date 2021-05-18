"""
https://leetcode.com/problems/find-duplicate-file-in-system/

Python parse practice
"""
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ref = collections.defaultdict(list)
        for path in paths:
            path = path.split(" ")
            root_path = path[0]
            for file in path[1:]:
                fname, fcontent = file.split('(')
                ref[fcontent].append(root_path + '/' + fname)
        ans = []
        for k in ref:
            if len(ref[k]) > 1:
                ans.append(ref[k])
        return ans