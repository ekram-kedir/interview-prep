class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = defaultdict(list)
        priority_queue = [(-1 , start)]
        distance = [0] * (n + 1)
        
        for index  in range(len(edges)):
            src , des = edges[index][0] , edges[index][1]
            graph[src].append((des , succProb[index]))
            graph[des].append((src , succProb[index]))
            
        while priority_queue:
            w , src = heapq.heappop(priority_queue)
            for neigh_des , neigh_w in graph[src]:
                if neigh_w * (-w) > distance[neigh_des]:
                    distance[neigh_des] = (neigh_w * (-w))
                    heapq.heappush(priority_queue , ( -(neigh_w * (-w)), neigh_des))
                    
        return distance[end]

            