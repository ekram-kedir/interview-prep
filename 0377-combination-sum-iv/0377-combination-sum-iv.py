class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        @cache
        def dp(curr_sum):
            
            if curr_sum == target:
                return 1
            
            if curr_sum > target:
                return 0
            
            pick = 0
            
            for idx in range(n):
                pick += dp(curr_sum + nums[idx]) 
            return pick 
        
        return dp(0)
            