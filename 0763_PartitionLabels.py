# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-labels/

1. Scan the string, store the last index of the chars in to a dictionary 
named 'last'. 
2. Find the divider that make the partition meets requirement. 
    Criteria:
    If i <= divider[-1], divider[-1] = max(divider[-1], last[s[i]])
    Else, divider.append(last[s[i]])
3. Use divider information to compute the length of each part.
"""
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Scan the string, get last index of each char
        last = {c: i for i, c in enumerate(S)}
      
        # Get divider information
        divider = [last[S[0]]]
        for i, c in enumerate(S):
            if i == 0:
                continue
            if i <= divider[-1]:
                divider[-1] = max(divider[-1], last[c])
            else:
                divider.append(last[c])
            
        # Compute length of each part
        ans = [divider[0] + 1]
        for i in range(1, len(divider)):
            ans.append(divider[i] - divider[i-1])
        return ans
