class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)
        players = list(zip(ages, scores))
        players.sort() 
        
        dp = [score for _, score in players]

        for i in range(n):
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)
