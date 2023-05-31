class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = defaultdict(int)
        def dp(curr_amount):
            
            if curr_amount < 0:
                return inf
            if curr_amount == 0:
                return 0
            if curr_amount in memo:
                return memo[curr_amount]
            
            best = float("inf")
            for c in coins:
                best = min(best , (dp(curr_amount - c) + 1))
            memo[curr_amount] = best
            return memo[curr_amount] 

        answer = dp(amount)
        return answer if answer != float("inf") else -1