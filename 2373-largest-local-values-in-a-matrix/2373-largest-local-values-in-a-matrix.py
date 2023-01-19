class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        def helper(grid, start ,end):
            max_value = 0
            for i in range(start ,start + 3):
                for j in range(end,end + 3):
                        max_value = max(max_value , grid[i][j])
            return max_value
        answer = [[0 for i in range(n - 2)]for j in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                answer[i][j] = helper(grid, i, j )
        return answer