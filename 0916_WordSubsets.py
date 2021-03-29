"""
https://leetcode.com/problems/word-subsets/

Use B to build a mask, where
mask[ch] = max(cnt[ch] for cnt in count(b) in B)

Then just check whether each a has no less character count than the mask. 

Time compleixty: O(M + N)
"""
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        mask = collections.defaultdict(int)
        for b in B:
            cnt = Counter(b)
            for ch in cnt:
                mask[ch] = max(mask[ch], cnt[ch])
        
        target_ch = []
        for ch in mask:
            if mask[ch] > 0:
                target_ch.append(ch)
        target_ch = set(target_ch)
        
        ans = []
        for a in A:
            cnt = Counter(a)
            if all(cnt[ch] >= mask[ch] for ch in target_ch):
                ans.append(a)
        return ans