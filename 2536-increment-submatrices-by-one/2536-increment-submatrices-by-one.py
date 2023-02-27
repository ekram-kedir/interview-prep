class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n  for j in range(n)]
        
        for row1,col1,row2,col2 in queries:
            for row in range(row1 , row2 + 1):
                mat[row][col1] += 1
                
                if col2 + 1 < n:
                    mat[row][col2 + 1] -= 1
                    
        for rows in mat:
            for col in range(1 , n):
                rows[col] += rows[col - 1]
        return mat