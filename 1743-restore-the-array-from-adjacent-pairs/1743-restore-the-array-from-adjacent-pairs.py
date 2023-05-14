class Solution:
    def dfs(self ,graph , visited , answer , node):
        
        if node in visited:
            return
        
        visited.add(node)
        answer.append(node)
        
        for ngh in graph[node]:
            if ngh not in visited:
                self.dfs(graph , visited , answer , ngh)
            
               
                   
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        graph = defaultdict(list)
        answer = []
        visited = set()
        
        for a,b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            
        for k,v in graph.items():
            if len(v) == 1:
                start = k
                break
        self.dfs(graph , visited , answer , start)
        return answer