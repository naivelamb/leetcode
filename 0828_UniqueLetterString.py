# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/unique-letter-string/

How many substrings have exactly one "A"?
Need to get all A indices, let's say we have S[i], S[j], S[k] as A.
The number of substrings containing S[i] and only one A is:
(i+1)*(j-i)
The number of substrings containing S[j] and only one A is:
(j-i)*(k-j)

Hence we need to first compute the index dictionary, then go over the dictionary
to get to answer.

Time complexity: O(N), N=len(S)
"""
import collections
class Solution:
    def uniqueLetterString(self, S: str) -> int:
        index = collections.defaultdict(list)
        for i, c in enumerate(S):
            index[c].append(i)

        ans = 0
        for idxs in index.values():
            idxs = [-1] + idxs + [len(S)]
            for i in range(1, len(idxs) - 1):
                ans += (idxs[i] - idxs[i-1]) * (idxs[i+1] - idxs[i])
        return ans % (10**9 + 7)


s = Solution()
string = "ABC"
assert (s.uniqueLetterString(string)) == 10

string = "ABA"
assert (s.uniqueLetterString(string)) == 8
