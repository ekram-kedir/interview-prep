class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        calculate_sum = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows - 2):
            for col in range(cols - 2):
                
                calculate = grid[row][col] + grid[row][col + 1] + grid[row][col + 2] + grid[row +1][col + 1] + grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
                
                calculate_sum = max(calculate , calculate_sum)
        return calculate_sum
                
                