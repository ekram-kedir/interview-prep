class UnionFind:
    
    def __init__(self,size):
        
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
        
    def find(self , row):
        
        if row == self.root[row]:
            return row
        self.root[row] = self.find(self.root[row])
        return self.root[row] 
    
    def union(self, row , col):
        
        first = self.find(row)
        second = self.find(col)
        
        if first != second:
            if self.rank[first] > self.rank[second]:
                self.root[second] = first
            elif self.rank[row] < self.rank[col]:
                self.root[first] = second
            else:
                self.root[second] = first
                self.rank[first] += 1
            self.count -= 1
            
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        f = UnionFind(n)
        
        for row , col in edges:
            f.union(row , col)
            
        return f.find(source) == f.find(destination)
            
        