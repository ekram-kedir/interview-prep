class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        answer = [0 for _ in range(len(queries))] 
        
        for index,key in enumerate(equations):
            src,des = key[0], key[1]
            graph[src].append((des , values[index]))
            graph[des].append((src , (1/ values[index])))
            
        
        def helper(start ,end ,cur_dist ,visited):
            
            queue = deque([[start, cur_dist]])
            
            while queue:
                
                cur_node , cur_weight = queue.popleft()
                if cur_node == end:
                    return cur_weight
                
                for curr_k, curr_v  in graph[cur_node]:
                    if curr_k not in visited:
                        visited.add(curr_k)
                        queue.append([curr_k , curr_v * cur_weight])  
                    
            return -1.0
        
        for index,key in enumerate(queries):
            start,end = key[0], key[1]
            visited = set()
            visited.add(start)
            
            if start in graph:
                answer[index] = helper(start , end , 1 , visited)
            else:
                answer[index] = -1.0
        
        return answer