class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        store = defaultdict(int)
        
        def dp(idx , curr_sum):
            
            if idx >= n:
                return curr_sum == target
            
            if (idx , curr_sum) in store:
                return store[(idx , curr_sum)]
            
            take_pos = dp(idx + 1, curr_sum - nums[idx]) 
            take_neg = dp(idx + 1 , curr_sum + nums[idx])
            
            store[(idx , curr_sum)] = take_pos + take_neg
            
            return store[(idx , curr_sum)]
        
        return dp(0 , 0)