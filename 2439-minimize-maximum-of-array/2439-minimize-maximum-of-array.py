class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        firstNum = nums[0]
        sumAll = nums[0]
        answer = nums[0]
        
        if max(nums) == nums[0]:
            return nums[0]
        
        for i in range(1,len(nums)):
            sumAll += nums[i]
            answer = max(answer , math.ceil(sumAll / (i + 1)))
        return answer