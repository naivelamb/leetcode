"""
https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

s = "xxxxAxxx", t = "Axxxxxxx"
The best way to move A to the most left, is move A one by one. Therefore, it requires that all element in the left are larger than A.

After that, we need to check s[1:] and t[1:].

Use queue to keep all the positions of 0 to 9 in s. For a number x in t, we know its most left position in s, then check all the smaller element to find if there is anyone locate at the more left postiion.

Since we only need to check 10 digits, time Complexity is O(10*n)
"""
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if collections.Counter(s) != collections.Counter(t): return False
        s = [*map(int, s)]
        t = [*map(int, t)]
        n = len(s)

        queue = collections.defaultdict(collections.deque)
        for i, x in enumerate(s):
            queue[x].append(i)

        for x in t:
            indx = queue[x].popleft()
            for i in range(x):
                if queue[i] and queue[i][0] < indx:
                    return False

        return True
