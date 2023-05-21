class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        length = len(isConnected) 
        visited = set()
        result = 0
        
        for i in range(length):
            for j in range(length):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        for node in range(length):
            if node not in visited:
                result += 1
                self.dfs(node, graph ,  visited)
                
        return  result
    
    def dfs(self,node , graph , visited):

        visited.add(node)
        for ngh in graph[node]:
            if ngh not in visited:
                self.dfs(ngh , graph , visited)
        
            
                    
            
            