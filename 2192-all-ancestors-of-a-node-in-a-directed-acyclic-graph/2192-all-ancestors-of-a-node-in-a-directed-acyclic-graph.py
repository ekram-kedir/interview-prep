class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]
        answer = [[] for _ in range(n)]
        queue = deque([])
        
        for a,b in edges:
            graph[a].append(b)
            incoming[b] += 1
            
        for node in range(n):
            
            if incoming[node] == 0:
                queue.append(node)
                
        while queue:
            
            node = queue.popleft()
            
            for ngh in graph[node]:
                
                if len(answer[node]) == 0:
                    answer[ngh].append((node))
                elif len(answer[node]) > 0:
                    for e in answer[node]:
                        if e not in  answer[ngh]:
                            answer[ngh].append(e)
                    answer[ngh].append((node))
                    answer[ngh].sort()
                incoming[ngh] -= 1
                
                if incoming[ngh] == 0:
                    queue.append(ngh)
                    
        return answer
            
            
        