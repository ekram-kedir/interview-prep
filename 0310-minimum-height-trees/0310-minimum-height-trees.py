class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for i in range(n)]
        connection = [0 for i in range(n)]
        answer = [0 for i in range(n)]
       
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            connection[a] += 1
            connection[b] += 1
            
        queue = deque([])
        
        for ind in range(n):
            if connection[ind] == 1:
                queue.append(ind)
        
        while queue:
            
            answer = [i for i in queue]
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for curr in graph[node]: 
                    connection[curr] -= 1
                    if connection[curr] == 1 :
                        queue.append(curr)


        return answer