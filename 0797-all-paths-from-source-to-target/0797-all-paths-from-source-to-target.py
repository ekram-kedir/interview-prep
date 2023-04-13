class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.dfs(0 ,[0],len(graph),graph)
        return self.result
    
    def dfs(self,node, path, n, graph):
        
        if node == n - 1:
            self.result.append(path[:])
        
        
        for node in graph[node]:
            path.append(node)
            self.dfs(node, path, n, graph)
            path.pop()