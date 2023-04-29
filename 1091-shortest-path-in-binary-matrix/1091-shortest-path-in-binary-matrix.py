class Solution:
    def check(self,index,length):
        
        if index[0] >= length[0] or index[0] < 0 or index[1] >= length[1] or index[1] < 0:
            return False
        return True
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] != 0:
            return -1
        if (len(grid) , len(grid[0])) == (1,1) and grid[0][0] == 0:
            return 1
        lengths = (len(grid) , len(grid[0]))
        visited = set()
        queue = deque([(0,0)])
        directions = [(0,-1),(0,1),(1,-1),(-1,1),(1,0),(-1,0),(-1,-1),(1,1)]
        count = 1
        
        while queue:
            
            if (lengths[0] - 1, lengths[1] - 1) in visited:
                return count
        
            length = len(queue)
            count += 1
            
            for  ele in range(length):
                node = queue.popleft()
                
                for d in directions:
                    if self.check((node[0] + d[0],node[1]+ d[1]) , lengths) == True and grid[node[0] + d[0]][node[1]+ d[1]] == 0 and (node[0]+ d[0],node[1]+ d[1]) not in visited:
                             visited.add((node[0] + d[0],node[1] + d[1]))
                             queue.append((node[0] + d[0],node[1] + d[1]))
                                
        print(visited)
                                
        return -1
                    
        
    

    
   
                   
                        