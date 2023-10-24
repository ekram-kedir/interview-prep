class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            while nums[left] % 2 != 0 and left < right:
                
                if nums[right] % 2 == 0:
                    nums[left], nums[right] = nums[right] , nums[left]
                    
                    left += 1
                    right -= 1
                    
                else:
                    right -= 1
            else:
                left += 1
                
        return nums
            