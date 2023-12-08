class Solution:
    def inBound(self, row, col, rows, cols):
        if col >= 0 and col < cols and row >= 0 and row < rows:
            return True
        return False
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dxns = [(-1,0), (1,0), (0,1), (0,-1)]
        number_of_islands = 0
        visited = set()
        
        def dfs(node):
            
            if node in visited:
                return
            
            visited.add(node)
            row, col = node
            for dr, dc in dxns:
                if ((row + dr, dc + col) not in visited) and self.inBound(dr + row, dc + col, rows, cols) and grid[row][col] == "1":
                    dfs(((dr + row),(dc + col)))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs((row,col))
                    number_of_islands += 1
        return number_of_islands
                    
            
            
                    
            
            
            