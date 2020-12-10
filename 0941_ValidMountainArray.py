"""
https://leetcode.com/problems/valid-mountain-array/

Find the peak and change tracing rule. 

Time complexity: O(N)
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] <= arr[0]:
            return False
        flag = True
        for i in range(1, len(arr)):
            if flag:
                if arr[i] > arr[i-1]:
                    pass
                elif arr[i] == arr[i-1]:
                    return False
                else:
                    flag = False
            else:
                if arr[i] < arr[i-1]:
                    pass
                else:
                    return False
        if flag:
            return False
        return True