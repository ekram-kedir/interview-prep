class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = set()
        area = 0
        
        for a in range(m):
            for b in range(n):
                if (a,b) not in visited and grid[a][b] == 1:
                    self.area = 0
                    self.dfs((a,b), visited , m , n , grid)
                    area = max(area,self.area)
        
        return area
    def dfs(self,node , visited , m , n , grid):
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        
        visited.add(node)
        self.area += 1
      
        for dx,dy in direction:
            if (dx + node[0]) < m and (dy + node[1]) < n and  (dx + node[0]) >= 0 and (dy + node[1]) >= 0 and ((node[0] + dx), (node[1] + dy)) not in visited and grid[node[0]+ dx][node[1] + dy] == 1:        
                self.dfs(((node[0] + dx), (node[1] + dy)),visited , m , n , grid)
       
    
        