class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        idx = defaultdict(list)
        
        def helper(col , row , element1 , element2):
            for j in range(col):
                    matrix[element1][j] = 0
            for i in range(row):
                    matrix[i][element2] = 0
        count = 0   
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    count += 1
                    idx[count].append(i)
                    idx[count].append(j)
        for value in idx.values():
            helper(col , row ,value[0],value[1])
                    