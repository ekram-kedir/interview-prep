class Solution: 
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        
        def dp(idx, robbed_last):
            
            if idx < 0:
                return 0
            
            if idx == 0 and robbed_last == True:
                return 0
            elif idx == 0 and robbed_last == False:
                return nums[0]
            
            if (idx, robbed_last) in memo:
                return memo[(idx, robbed_last)]
            
            memo[(idx, robbed_last)] = max(dp((idx - 1),robbed_last) , nums[idx] + dp((idx - 2), robbed_last))
            return memo[(idx, robbed_last)]
        
        rob = dp((len(nums)-3),True) + nums[-1]
        no_rob = dp((len(nums)-2),False)
        
        return max(no_rob , rob)
            