# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reorganize-string/

Count all characters in the string, push them into a heap as pair: (-cnt, ch)
If any cnt > (len(S) + 1)//2, then it is not possible to rearrange the string,
return ''.
Then we arrange the string such that the most frequent char followed by the 2nd most
frequent char. 

Time complexity: O(n + nlog26)
"""
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        ref = {}
        for ch in S:
            ref[ch] = ref.get(ch, 0) + 1
            if ref[ch] > (len(S) + 1) // 2:
                return ''
        heap = [(-ref[ch], ch) for ch in ref]
        heapq.heapify(heap)
        ans = []
        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)
            ans.extend([ch1, ch2])
            if cnt1 + 1: heapq.heappush(heap, (cnt1 + 1, ch1))
            if cnt2 + 1: heapq.heappush(heap, (cnt2 + 1, ch2))
        return ''.join(ans) + (heap[0][1] if heap else '')

s = Solution()
S = 'aab'
print(s.reorganizeString(S))