class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        
        direction = [[-1 , 0] , [0 , -1] , [1 , 0] , [0 , 1]]
        visited = set()
        
        priority_queue = [[grid[0][0] , 0 , 0]]
        visited.add((0 , 0))
        
        while priority_queue:
            
            current_distance ,r , c = heapq.heappop(priority_queue)
            
            if r == row - 1 and c == col - 1:
                return current_distance
            
            for dr , dc in direction:
                new_r , new_c = dr + r , dc + c
                if new_r < 0 or new_c < 0 or new_r == row or new_c == col or (new_r , new_c) in visited:
                    continue
                visited.add((new_r , new_c))
                heapq.heappush(priority_queue , [max(current_distance , grid[new_r][new_c]) , new_r , new_c])
            
            
                    