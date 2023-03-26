class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < len(nums):
            
            if nums[i] != i and nums[i] == len(nums):
                 i += 1
            elif nums[i] != i:
                reference = nums[i]
                nums[i] , nums[reference] = nums[reference] , nums[i]
            else:
                i += 1
          
        if len(nums) in nums:
            return nums.index(len(nums))
        else:
            return len(nums)
            