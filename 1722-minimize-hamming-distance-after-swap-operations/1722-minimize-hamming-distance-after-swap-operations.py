class Solution:
    def find(self , x , array):
        
        if x != array[x]:
            array[x] = self.find(array[x] , array)
        return array[x]
    
    def union(self , x , y , array):
        
        rootX = self.find(x , array)
        rootY = self.find(y , array)
        
        if self.rankTarget[rootX] >= self.rankTarget[rootY]:
            array[rootY] = rootX
            self.rankTarget[rootX] += self.rankTarget[rootY]
        else:
            self.rankTarget[rootX] < self.rankTarget[rootY]
            array[rootX] = rootY
            self.rankTarget[rootY] += self.rankTarget[rootX]
    def unionSource(self , x , y , array):
        
        rootX = self.find(x , array)
        rootY = self.find(y , array)
        
        if self.rankSource[rootX] >= self.rankSource[rootY]:
            array[rootY] = rootX
            self.rankSource[rootX] += self.rankSource[rootY]
        else:
            self.rankSource[rootX] < self.rankSource[rootY]
            array[rootX] = rootY
            self.rankSource[rootY] += self.rankSource[rootX]
                                                      
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        length = len(source)
        index = {i:i for i in range(length)}
        self.rankTarget = [1] * length
        hammingDistance = 0
       
        for a,b in allowedSwaps:
            self.union(a,b, index)
        
        graph = defaultdict(list)
        
        for k,v in index.items():
            graph[self.find(k,index)].append(k)
       
        for v in graph.values():
            getSource = [source[i] for i in v]
            getTarget = [target[i] for i in v]
            count = defaultdict(int)

            for val in getSource:
                count[val] += 1

            for val in getTarget:
                if count[val] > 0:
                    count[val] -= 1
                else:
                    hammingDistance += 1

        return hammingDistance