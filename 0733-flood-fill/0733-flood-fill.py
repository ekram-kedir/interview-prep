class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        lengths = [len(image),len(image[0])]
        source = image[sr][sc]
        temp = source
        
        def dfs(visited,curr_index,lengths):
            
            if curr_index[0] >= lengths[0] or curr_index[0] < 0 or curr_index[1] < 0 or curr_index[1] >= lengths[1]:
                return
            if image[curr_index[0]][curr_index[1]] == temp:
                    image[curr_index[0]][curr_index[1]] = color
            else:
                return
         
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            visited.add(curr_index)
           
            
            for node in directions:

                if (curr_index[0]+ node[0],curr_index[1]+ node[1]) not in visited:
                    dfs(visited,(curr_index[0]+ node[0],curr_index[1]+ node[1]),lengths)
        
        
        dfs(set(), (sr,sc),lengths)
        return image
           