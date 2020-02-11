"""
https://leetcode.com/problems/circular-array-loop/

Each point can be a starting point, the direction should be the same, which is determined by the starting point.

We also need to store the circle length, to make sure it is > 2.

Time complexity: O(N^2)
"""
class Solution:
    def circularArrayLoop(self, nums) -> bool:
        n = len(nums)
        for i in range(n):
            p = i
            length = 0
            orders = [i]
            visited = set(orders)
            if nums[i] > 0:
                dir = 1
            else:
                dir = -1
            while True:
                jump = nums[p % n]
                if jump * dir < 0:
                    break
                length += 1
                if (p + jump) % n in visited:
                    if (p + jump) % n != orders[-1]:
                        return True
                    else:
                        break
                if length > n:
                    break
                p += jump
                visited.add(p)
                orders.append(p%n)
        return False

sol = Solution()
assert sol.circularArrayLoop([2,-1,1,2,2]) == True
assert sol.circularArrayLoop([-1,2]) == False
assert sol.circularArrayLoop([-2,1,-1,-2,-2]) == False
assert sol.circularArrayLoop([2,2,2,2,2,4,7]) == False
