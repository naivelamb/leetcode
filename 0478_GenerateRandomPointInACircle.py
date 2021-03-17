"""
https://leetcode.com/problems/generate-random-point-in-a-circle/

Sample point in the ([x_center - r, x_center + r], [y_center - r, y_center + r]), reject if distance to center is larger than radius.


"""
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self) -> List[float]:
        x = random.uniform(-1, 1) * self.radius + self.x_center
        y = random.uniform(-1, 1) * self.radius + self.y_center
        while (x - self.x_center) ** 2 + (y - self.y_center) ** 2 > self.radius**2:
            x = random.uniform(-1, 1) * self.radius + self.x_center
            y = random.uniform(-1, 1) * self.radius + self.y_center            
        return [x, y]
    
    def randPoint_polar(self):
        theta = random.uniform(0, 2 * math.pi)
        R = self.r*math.sqrt(uniform(0, 1))
        return [self.x_center + R * math.cos(theta), self.y_center + R * math.sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()