class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dp(row,col):
            
            if row == m - 1 and col == n - 1:
                return 1
            if row + 1 < m and col + 1 < n:
                return dp(row + 1,col) + dp(row , col + 1)
            if row + 1 < m and col + 1 == n:
                return dp(row + 1, col)
            if row + 1 == m and col + 1 < n:
                return dp( row, col + 1)
            
        return dp(0 , 0)
                