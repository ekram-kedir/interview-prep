class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        dp[0] = matrix[0][:]

        for row in range(1, rows):
            for col in range(cols):
                # Handle boundary cases
                if col == 0:
                    dp[row][col] = min(dp[row - 1][col], dp[row - 1][col + 1]) + matrix[row][col]
                elif col == cols - 1:
                    dp[row][col] = min(dp[row - 1][col], dp[row - 1][col - 1]) + matrix[row][col]
                else:
                    dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1]) + matrix[row][col]

        # Find the minimum sum in the last row
        return min(dp[-1])