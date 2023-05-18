class UnionFind:
    
    def __init__(self, size):
        
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self , row):
        
        if row == self.root[row]:
            return row
        self.root[row] = self.find(self.root[row])
        return self.root[row]
    
    def union(self , row , col):
        root_row = self.find(row)
        root_col = self.find(col)
        
        if root_row != root_col:
            if self.rank[root_row] > self.rank[root_col]:
                self.root[root_col] = root_row
            elif self.rank[root_col] > self.rank[root_row]:
                self.root[root_row] = root_col
            else:
                self.root[root_col] = root_row
                self.rank[root_row] += 1
    def pr(self):
        return self.root
                
class Solution:
    def validBoundary(self,row , col , m , n):
        return  row >= 0 and row < m and col >= 0 and col < n
    def findNeighbours(self , row , col , grid):
        m = len(grid)
        n = len(grid[0])
        direction = {
            1:[(0,-1) , (0,1)],
            2:[(-1,0) , (1,0)],
            3:[(0,-1) , (1,0)],
            4:[(0,1) , (1,0)],
            5:[(0,-1) , (-1,0)],
            6:[(0, 1), (-1, 0)]
        }
        node = grid[row][col]
        result = []
        
        for a,b in direction[node]:
            c,d = row + a , col + b
            if self.validBoundary(c,d , m , n) and (-a,-b) in direction[grid[c][d]]:
                result.append((c,d))
        return result
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        f = UnionFind(m * n)
        
        for r in range(m):
            for c in range(n):
                node = r * n + c
                result = self.findNeighbours(r , c , grid)
                for  a,b in result:
                    ngh = a * n + b
                    f.union(node , ngh)
                    
        return f.find(0) == f.find(m * n - 1)