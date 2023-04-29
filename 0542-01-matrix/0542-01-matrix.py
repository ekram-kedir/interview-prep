class Solution:
    def check(self,index,length):
        
        if index[0] >= length[0] or index[0] < 0 or index[1] >= length[1] or index[1] < 0:
            return False
        return True
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        lengths = (len(mat) , len(mat[0]))
        visited = set()
        queue = deque([])
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        answer = [[0 for _ in range(lengths[1])] for _ in range(lengths[0])]
        count = 0
        
        for row in range(lengths[0]):
            for col in range(lengths[1]):
                if mat[row][col] == 0:
                    queue.append((row,col))
                    visited.add((row,col))
        
        while queue:
            count += 1
            length = len(queue)
            
            for  ele in range(length):
                node = queue.popleft()
                
                
                answer[node[0]][node[1]] = count - 1
                
                for d in directions:
                    if self.check((node[0] + d[0],node[1]+ d[1]) , lengths) == True and (node[0]+ d[0],node[1]+ d[1]) not in visited:
                             visited.add((node[0] + d[0],node[1] + d[1]))
                             queue.append((node[0] + d[0],node[1] + d[1]))
                          
               
                
        return answer
                    