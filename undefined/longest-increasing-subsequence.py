class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = [1 for _ in range(len(nums))]
        
        
        for ind in range(1,len(nums)):
            for index in range(ind):
                if nums[ind] > nums[index]:
                    memo[ind] = max(memo[ind] , memo[index] + 1)
                    
        return max(memo)
        