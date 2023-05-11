
from typing import List
class Solution:
    def dfs(self ,node , graph, colors , parent):
        if colors[node] == 2:
            return 0
        if colors[node] == 1:
            return 1
            
        colors[node] = 1
        for ngh in graph[node]:
            if ngh != parent and self.dfs(ngh, graph , colors, node):
                return 1
                
        colors[node] = 2
        return 0
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
		colors = [0 for _ in range(len(adj))]
		parent = 'ekram'
		for ind in range(len(adj)):
		    if self.dfs(ind, adj , colors , parent):
		        return True
		return False
		
