class Solution:
    def dfs(self , node , graph , colors):
        
        if colors[node] == 2:
            return False
        
        if colors[node] == 1:
            return True
        
        colors[node] = 1
        
        for ngh in graph[node]:
            if self.dfs(ngh , graph , colors):
                return True
            
        
        colors[node] = 2
        
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses)]
        
        for a,b in prerequisites:
            graph[b].append(a)
            
        for a in range(numCourses):
            
            if self.dfs(a , graph , colors):
                return False
            
        return True
        