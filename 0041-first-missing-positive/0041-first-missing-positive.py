class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
       
        pointer = 0
        length = len(nums)
        
        while pointer < length:
            reference = nums[pointer]
            
            if nums[pointer] != pointer + 1 and nums[pointer] > 0 and nums[pointer] <= length and nums[pointer] != nums[reference - 1]:
                nums[pointer] , nums[reference - 1] = nums[reference - 1] , nums[pointer]
            else:
                pointer += 1
        for num in range(len(nums)):
            if nums[num] != num + 1:
                return num + 1
         
        return length + 1