class Solution:
    
    def longestPalindromeSubseq(self, s: str) -> int:
        
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        
        for i in range(N):
            dp[i][i] = 1
            
        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The result is stored in dp[0][N-1]
        return dp[0][N - 1]