class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        priority_queue = [(0 , k)]
        visited = set()
        t = 0
        
        for src , des , w in times:
            graph[src].append((des , w))
            
        while priority_queue:
            
            w , src = heapq.heappop(priority_queue)
            if src in visited:
                continue
                
            visited.add(src)
            t = max(t , w)
            
            for neigh in graph[src]:
                neigh_des , neigh_w = neigh
                
                if neigh_des not  in visited:
                    heapq.heappush(priority_queue , (neigh_w + w , neigh_des))
                    
        return t if len(visited) == n else -1
