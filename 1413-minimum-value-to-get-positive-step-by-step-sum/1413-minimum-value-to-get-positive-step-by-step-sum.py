class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue=1000
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            startValue=min(startValue,total)
        return abs(startValue)+1 if startValue<0 else 1
        
        
            