class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        digit = ""
        for i in nums:
            digit += str(i)
            
        digitSum = 0
        for i in digit:
            digitSum += int(i)
            
        elementSum = sum(nums)
        
        return abs(elementSum - digitSum)