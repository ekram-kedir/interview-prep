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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        answer = []
        f = UnionFind(len(edges))
        
        for a,b in edges:
            
            if f.find(a - 1) == f.find(b - 1):
                answer.append([a,b])
            f.union(a - 1,b - 1)
            
                
        return answer[-1]