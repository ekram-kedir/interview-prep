class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @cache
        def dp(cur_index , total):
            
            if total < 0 or cur_index >= len(nums):
                return False
            if total == 0:
                return True
            
            return dp(cur_index + 1,total - nums[cur_index] ) or dp(cur_index + 1, total)
            
        halfSum = sum(nums) / 2
        
        if sum(nums) % 2 != 0:
            return False
        else:
            return dp(0 , halfSum )
            
        