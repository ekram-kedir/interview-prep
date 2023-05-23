class Solution:
    def find(self, x):
        
        if self.points[x] != x:
            self.points[x] = self.find(self.points[x])
        return self.points[x]
    
    def union(self, x, y):
        
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] >= self.rank[rootY]:
                self.points[rootX] = rootY
                self.rank[rootY] += self.rank[rootX] 
                
            elif self.rank[rootX] < self.rank[rootY]:
                self.points[rootY] = rootX
                self.rank[rootX] += self.rank[rootX] 
            
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        self.points = {(a,b): (a,b) for a,b in points}
        self.rank = {(a,b): 1 for a,b in points}
        edges = []
        total = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    a,b = points[i]
                    e,d = points[j]
                    cal = abs(a - e) + abs(b - d)
                    edges.append(((a,b) ,(e,d), (cal)))
                    
        edges = sorted(edges, key = lambda x: x[2])
        
        for i,j,k in edges:
            
            if self.find(i) != self.find(j):
                self.union(i , j)
                total += k
        
        return total
