class Solution:
    def find(self , x):
        if self.stones[x] != x:
            self.stones[x] = self.find(self.stones[x] )
        return self.stones[x] 
    
    def union(self,x ,y):
        
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.stones[rootY] = rootX
            
    def removeStones(self, stones: List[List[int]]) -> int:
        
        size = len(stones)
        self.stones = {(a,b):(a,b) for a,b in stones}
        self.rank = [1] * size
        
        for i in range(size):
            for j in range(size):
                
                 a,b = stones[i]
                 c,d = stones[j]
                 
                 if a == c or b == d:
                    self.union((a,b) , (c,d))
           
        for i in range(size):
            for j in range(size):
                
                 a,b = stones[i]
                 c,d = stones[j]
                 
                 if a == c or b == d:
                    self.union((a,b) , (c,d))
                    
        answer = set()
        for a,b in stones:
            answer.add(self.stones[(a,b)])
            
        return size - len(answer)
            
        