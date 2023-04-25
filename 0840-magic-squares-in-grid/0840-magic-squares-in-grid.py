class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
         
        count = 0
        
        def check(submatrix):
            flag = True
            for i in range(3):
                for j in range(3):
                  if submatrix[i][j] < 1 or submatrix[i][j] > 9:
                     flag = False
            for i in range(3):
                if len(set(submatrix[i])) != 3 or sum(submatrix[i]) != 15:
                    flag = False
            for i in zip(*submatrix):
                if len(set(i)) != 3 or sum(list(i)) != 15:
                    flag = False
                    
            if submatrix[0][0] + submatrix[1][1] + submatrix[2][2] != 15:
                flag = False
                
            if submatrix[0][2] + submatrix[1][1] + submatrix[2][0] != 15:
                flag = False
           
            return flag
        
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows - 2):
            for j in range(cols - 2):
                submatrix = [grid[x][j:j+3] for x in range(i,i+3)]
                if check(submatrix) == True:
                    count += 1
        return count
        

                
                