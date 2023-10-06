class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [1] * (n + 1)
        
        if n <= 3:
            return n - 1
        
        dp[2] = 2
        dp[3] = 3
        
        for num in range(4 , n + 1):
            dp[num] = max( 2 * dp[num - 2] , 3 * dp[num - 3])
            
        return dp[n]
            