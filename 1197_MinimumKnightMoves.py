"""
https://leetcode.com/problems/minimum-knight-moves/

Naive BFS, time complexity: O(max(|x|, |y|)^2)


"""
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        origin_queue = deque([(0, 0, 0)])
        origin_distance = {(0, 0): 0}

        target_queue = deque([(x, y, 0)])
        target_distance = {(x, y): 0}
        
        while True:
            origin_x, origin_y, origin_steps = origin_queue.popleft()
            if (origin_x, origin_y) in target_distance:
                return origin_steps + target_distance[(origin_x, origin_y)]
            
            target_x, target_y, target_steps = target_queue.popleft()
            if (target_x, target_y) in origin_distance:
                return target_steps + origin_distance[(target_x, target_y)]
            
            for dx, dy in moves:
                nx, ny = origin_x + dx, origin_y + dy
                if (nx, ny) not in origin_distance:
                    origin_queue.append((nx, ny, origin_steps + 1))
                    origin_distance[(nx, ny)] = origin_steps + 1
                
                nx, ny = target_x + dx, target_y + dy
                if (nx, ny) not in target_distance:
                    target_queue.append((nx, ny, target_steps + 1))
                    target_distance[(nx, ny)] = target_steps + 1
        
        