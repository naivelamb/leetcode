"""
https://leetcode.com/problems/can-place-flowers/
Go through all flowerbed, check the neighbors and place flower if available, find the maximum number of flowers we can place, then compare this number with n. 

Time complexity: O(N), N = len(flowerbed)
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        t = 0
        for i in range(len(flowerbed)):
            prev, after = False, False
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i-1] == 0:
                    prev = True
                if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                    after = True
                if prev and after:
                    t += 1
                    flowerbed[i] = 1

        return t >= n