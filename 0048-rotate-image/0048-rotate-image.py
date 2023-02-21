class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        answer = []

        for col in range(cols):
            answer = []
            for row in range(rows - 1,-1,-1):
                answer.append(matrix[row][col])
            result.append(answer)
            
        for row in range(len(result)):
            for col in range(len(result[0])):
                matrix[row][col] = result[row][col]
            
        print(str(list(map(list, result))).replace(', ', ','))

        
            