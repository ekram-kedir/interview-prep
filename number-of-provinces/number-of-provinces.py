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
                
            
            
            
    def getCount(self):
        return self.count
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        if not isConnected or len(isConnected) == 0:
            return 0
        
        length = len(isConnected)
        f = UnionFind(length)
        
        for c in range(length):
            for r in range(c + 1 , length):
                if isConnected[c][r] == 1:
                    f.union(c , r)
                    
        return f.getCount()        
        
        