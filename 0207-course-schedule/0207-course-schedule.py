class Solution:
    def dfs(self , node , graph, colors , order):
        
        if colors[node] == 1:
            return False
        
        colors[node] = 1
        
        for cur_node in graph[node]:
            
            if colors[cur_node] == 2:
                continue
                
            if not self.dfs(cur_node , graph, colors , order):
                return False
                
        colors[node] = 2
        order.append(node)
        return True
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses)]
        order = []
        
        for a,b in prerequisites:
            graph[b].append(a)
        
        
        for node in range(numCourses):
            
            if colors[node] != 0:
                continue
            if not self.dfs(node , graph, colors , order):
                return []
            
        return order
    
        
        