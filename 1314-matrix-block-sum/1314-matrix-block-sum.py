class Solution:
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]
        return result
    
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        n , m = len(matrix[0]) , len(matrix)
        self.pre_sum = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1,m + 1):
            for j in range(1,n + 1):
                self.pre_sum[i][j] = matrix[i - 1][j -1] - self.pre_sum[i - 1][j -1] + self.pre_sum[i - 1][j] + self.pre_sum[i][j- 1]
        

        for i in range(m):
            for j in range(n):
                row1, row2 , col1 , col2 = max((i - k) , 0) , min((i + k), (m - 1)) , max((j - k), 0 )  , min((j + k) , (n - 1))
                matrix[i][j] = self.sumRegion(row1,col1,row2,col2)
        return matrix
        
