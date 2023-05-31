class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        result = [[0 for i in range(m)] for j in range(n)]
        
        result[0][0] = 1
        
        for row in range(n):
            for col in range(m):
              
                if row > 0 and col == 0:
                    result[row][col] += result[row - 1][col]
                if row == 0 and col > 0:
                    result[row][col] += result[row][col - 1]
                if row > 0 and col > 0:
                    result[row][col] += result[row - 1][col] + result[row][col - 1]
                    
        return result[n - 1][m - 1]
             
                