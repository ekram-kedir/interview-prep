class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        priority_queue = [( 0 , 0 , src)]
        distance = defaultdict(lambda:inf)
        visited = set()
        
        for source , destination , price in flights:
            graph[source].append((destination , price))
        
        distance[src] = 0
        while priority_queue:
            
            stops, price, cur_node = heappop(priority_queue)
            if stops > k:
                break
            
            for next_node, next_price in graph[cur_node]:
                if next_node not in distance or distance[next_node] > price + next_price:
                    distance[next_node] = price + next_price
                    heappush(priority_queue, (stops + 1, next_price + price, next_node))
                    
        return distance[dst] if distance[dst] != inf else -1
        