class Solution:

    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        
        def dp(idx):
            
            if idx == 0:
                return nums[idx]
        
            if idx == 1:
                return max(nums[0],nums[1])
            if idx in memo:
                return memo[idx]
            
            memo[idx] = max(dp(idx - 1), nums[idx] + dp(idx - 2))
            return memo[idx]
        return dp(len(nums) - 1)
        