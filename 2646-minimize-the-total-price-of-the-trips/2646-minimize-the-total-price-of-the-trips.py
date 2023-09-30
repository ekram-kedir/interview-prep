class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        visitation = [0] * n
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def calculate(start, end , path):
            
            path.add(start)
            visited.add(start)
            
            if start == end:
                
                for node in path:
                    visitation[node] += 1
                    
                return True
            
            for neigh in graph[start]:
                if neigh not in visited and calculate(neigh , end , path):
                    return True
                
            path.remove(start)
            return False
        for src,des in trips:
            visited = set()
            calculate(src , des , set())
        
        dp = {}
        def dfs(node , parent , halve):
            
            if (node , halve) in dp:
                return dp[(node , halve)]
            
            halved = float("inf")
            
            if not halve:
                halved = visitation[node] * (price[node] // 2)
                for neigh in graph[node]:
                    if neigh != parent:
                        halved += dfs(neigh , node , True)
                    
            not_halved = visitation[node] * price[node]
            for neigh in graph[node]:
                if neigh != parent:
                    not_halved += dfs(neigh , node , False)
            dp[(node , halve)] = min(halved , not_halved)
                    
            return dp[(node , halve)]
        return dfs(0 , -1 , False)
        