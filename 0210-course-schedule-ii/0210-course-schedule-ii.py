class Solution:
    def dfs(self , node , graph , colors ,answer):
        
        if colors[node] == 2:
            return False
        
        if colors[node] == 1:
            return True
        
        colors[node] = 1
        
        for ngh in graph[node]:
            if self.dfs(ngh , graph , colors , answer):
                return True
            
        
        colors[node] = 2
        answer.append(node)
        
        return False
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses)]
        answer = []
        
        for a,b in prerequisites:
            graph[a].append(b)
            
        for a in range(numCourses):
            
            if self.dfs(a , graph , colors , answer):
                return []
            
        return answer
        