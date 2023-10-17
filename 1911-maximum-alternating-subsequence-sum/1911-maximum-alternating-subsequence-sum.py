class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        max_odd = (nums[0])
        max_even = (0)
        
        for index in range(1,len(nums)):
            max_odd = max(max_odd , nums[index] ,nums[index] + max_even)
            max_even = max(max_even , max_odd - nums[index])
            
        return max(max_even , max_odd)

