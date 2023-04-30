class Solution:
    def check(self,index,length):
        
        if index[0] >= length[0] or index[0] < 0 or index[1] >= length[1] or index[1] < 0:
            return False
        return True
    
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        lengths = (len(maze) , len(maze[0]))
        visited = set()
        queue = deque([entrance])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        deadends = set()
        
        for row in range(lengths[0]):
            for col in range(lengths[1]):
                if maze[row][col] == "+":
                    deadends.add((row,col))
        
        exits = set()
        
        for row in range(lengths[0]):
            for col in range(lengths[1]):
                if row == 0:
                    exits.add((row,col))
                elif row == lengths[0] - 1:
                    exits.add((row,col))
                elif col == 0:
                    exits.add((row,col))
                elif col == lengths[1] - 1:
                    exits.add((row,col))
        
        (a,b) = entrance
        exit = exits - deadends
        visited.add((a,b))
        if (a,b) in exit:
            exit.remove((a,b))
    
        count = 0
        
        while queue:

            length = len(queue)
            count += 1
            for ele in range(length):
                node = queue.popleft()
                (a,b) = node
                
                if (a,b) in exit:
                    return count - 1
                
                for d in directions:
                    if self.check((node[0] + d[0], node[1] + d[1]),lengths) == True and  (node[0] + d[0], node[1] + d[1]) not in visited and (node[0] + d[0], node[1] + d[1]) not in deadends:
                        visited.add((node[0] + d[0], node[1] + d[1]))
                        queue.append((node[0] + d[0], node[1] + d[1]))
                
               
        return -1