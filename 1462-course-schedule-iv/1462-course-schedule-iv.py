class Solution:
    def dfs(self, node, graph, visited, check, answer):
        if node in visited:
            return False
        
        visited.add(node)
        
        for ngh in graph[node]:
            
            if ngh == check:
                return True
            if self.dfs(ngh, graph, visited, check, answer):
                return True
        
        return False
    
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        answer = []
        
        for a, b in prerequisites:
            graph[b].append(a)
       
        for c, d in queries:
            
            visited = set()
            
            if graph[d]:
                answer.append(self.dfs(d, graph, visited, c, answer))
            else:
                answer.append(False)
          
        return answer
