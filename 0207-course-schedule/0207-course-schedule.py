class Solution:
    def dfs(self , node , graph , visited , callStack):
        
        if node in visited:
            return False
        
        if node in callStack:
            return True
        
        callStack.add(node)
        
        for ngh in graph[node]:
            if self.dfs(ngh , graph , visited , callStack):
                return True
            
        visited.add(node)
        callStack.remove(node)
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        
        for a,b in prerequisites:
            graph[b].append(a)
            
        visited = set()
        callStack = set()
        
        for a in range(numCourses):
            if self.dfs(a , graph , visited , callStack):
                return False
        return True
        