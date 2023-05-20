class Solution:
    def find(self, x):
        
        if self.roads[x] != x:
            self.roads[x] = self.find(self.roads[x])
        return self.roads[x]
    
    def union(self, x, y , cost):
        
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] >= self.rank[rootY]:
                self.roads[rootX] = rootY
                self.rank[rootY] = min(self.rank[rootX] , self.rank[rootY], cost)
                
            elif self.rank[rootX] < self.rank[rootY]:
                self.roads[rootY] = rootX
                self.rank[rootX] = min(self.rank[rootX] , self.rank[rootY], cost)
            
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        self.roads = {i: i for i in range(1,n+1)}
        self.rank = [float('inf')] * (n + 1)
        
        roads.sort(key=lambda x: x[2])  
        
        for a, b, c in roads:
            self.union(a, b , c)
       
        return self.rank[self.find(n)]
        
       
