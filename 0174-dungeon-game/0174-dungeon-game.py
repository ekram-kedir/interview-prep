class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        rows = len(dungeon)
        cols = len(dungeon[0])

        dp = [[0] * cols for _ in range(rows)]

        dp[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])

        for col in range(cols - 2, -1, -1):
            dp[rows - 1][col] = max(dp[rows - 1][col + 1] - dungeon[rows - 1][col], 1)

        for row in range(rows - 2, -1, -1):
            dp[row][cols - 1] = max(dp[row + 1][cols - 1] - dungeon[row][cols - 1], 1)

        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                min_points = min(dp[row + 1][col], dp[row][col + 1])
                dp[row][col] = max(min_points - dungeon[row][col], 1)

        return dp[0][0]
