class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        answer = [] 
        
        for index,key in enumerate(equations):
            src,des = key[0], key[1]
            graph[src].append((des , values[index]))
            graph[des].append((src , (1/ values[index])))
            
        
        def helper(start ,end):
            if start not in graph:
                return -1
            
            visited =set([start])
            queue = deque([[start, 1]])
            
            while queue:
                
                cur_node , cur_weight = queue.popleft()
                if cur_node == end:
                    return cur_weight
                
                for curr_k, curr_v  in graph[cur_node]:
                    if curr_k not in visited:
                        visited.add(curr_k)
                        queue.append([curr_k , curr_v * cur_weight])  
                    
            return -1
        
        for key,value in (queries):            
            answer.append(helper( key, value))
        
        return answer