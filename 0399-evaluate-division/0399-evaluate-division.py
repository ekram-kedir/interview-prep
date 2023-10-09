class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        answer = [0 for _ in range(len(queries))] 
        
        for index,key in enumerate(equations):
            src,des = key[0], key[1]
            graph[src].append((des , values[index]))
            graph[des].append((src , (1/ values[index])))
            
        
        def dfs(start ,end ,cur_dist ,visited):
            
            if start == end:
                return cur_dist
            
            
            for neigh in graph[start]:
                cur_node, cur_weight = neigh[0] , neigh[1]
                if cur_node not in visited:
                    visited.add(cur_node)
            
                    res = dfs(cur_node ,end ,  cur_weight * cur_dist , visited)
                    if res != -1:
                        return res
                
            return -1.0
        
        for index,key in enumerate(queries):
            start,end = key[0], key[1]
            visited = set()
            visited.add(start)
            
            if start in graph:
                answer[index] = dfs(start , end , 1 , visited)
            else:
                answer[index] = -1.0
        
        return answer