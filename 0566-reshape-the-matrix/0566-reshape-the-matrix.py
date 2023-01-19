class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        result = r * c
        
        if result != row * col:
            return mat
        
        answer = [[0 for i in range(c)]for j in range(r)]
        for i in range(result):
            answer[i // c][i % c] = mat[i // col][i % col]
        return answer