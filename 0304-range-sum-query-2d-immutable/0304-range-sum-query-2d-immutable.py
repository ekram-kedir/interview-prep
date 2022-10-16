class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col=len(matrix),len(matrix[0])
        self.total=[[0]*(col+1) for r in range(row+1)]
        
        for r in range(row):
            prefix=0
            for c in range(col):
                prefix+=matrix[r][c]
                above=self.total[r][c+1]
                self.total[r+1][c+1]=prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        start=self.total[row2+1][col2+1]
        end=self.total[row1][col2+1]
        left=self.total[row2+1][col1]
        right=self.total[row1][col1]
        return start-end-left+right

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)