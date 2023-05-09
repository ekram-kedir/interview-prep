class Solution:
        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node, graph , colors , result):
            if colors[node] == 1:
                return False

            colors[node] = 1

            for neighbour in graph[node]:
                if colors[neighbour] == 2:
                    continue
                if not dfs(neighbour, graph , colors , result):
                    return False

            colors[node] = 2
            result.append(node)
            return True

        
        colors = [0 for _ in range(len(graph))]
        result = []
        
        for node in range(len(graph)):
            if colors[node] != 0:
                continue
            
            dfs(node, graph , colors , result)
            result.sort()
            
        return result 