class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        length = len(triangle[-1])
        dp = [[inf for i in range(length)] for j in range(length)]
        dp[0][0] = triangle[0][0]
        print(dp)
        for row in range(1,length):
            for col in range(len(triangle[row])):
                    dp[row][col] = min(dp[row - 1][col] + triangle[row][col],dp[row - 1][col -1]+ triangle[row][col])
                 
        return min(dp[-1])
                