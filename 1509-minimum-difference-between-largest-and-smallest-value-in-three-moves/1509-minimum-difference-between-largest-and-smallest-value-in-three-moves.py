class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        nums.sort()
        
        if n <= 4:
            return 0
        
        else:
            
            first = nums[-1] - nums[3]
            second = nums[-2] - nums[2]
            third = nums[-3] - nums[1]
            fourth = nums[-4] - nums[0]
            return min(first ,second , third , fourth)
          
        
       
        
        