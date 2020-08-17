"""
https://leetcode.com/problems/distribute-candies-to-people/

Solve the function to get the number of distribution. Then compute rows & cols, calculate candies to each person.

Complexity: O(N), N = num_people
"""
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        p = int((2*candies + 0.25)**0.5 - 0.5)
        remain = candies - int((1 + p) * p / 2)
        rows, cols = p // num_people, p % num_people

        d = [0] * num_people
        for i in range(num_people):
            d[i] = (i+1)*rows + int(rows*(rows-1)/2)*num_people
            if i < cols:
                d[i] += i + 1 + rows*num_people
        d[cols] += remain
        return d
