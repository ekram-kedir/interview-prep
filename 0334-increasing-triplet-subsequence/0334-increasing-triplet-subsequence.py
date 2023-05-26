class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        smallest = inf
        pairs = [inf,inf]
        
        for i in range(len(nums)):
            
            if pairs[0] == inf:
                pairs[0] = nums[i]
            elif nums[i] > pairs[0] and pairs[1] == inf:
                pairs[1] = nums[i]
            elif pairs[1] > nums[i] and nums[i] > pairs[0]:
                pairs[1] = nums[i]
            elif pairs[1] > nums[i] and nums[i] >  smallest:
                pairs[0] = smallest
                pairs[1] = nums[i]
            elif nums[i] < pairs[0]:
                smallest = nums[i]
            elif nums[i] > pairs[1]:
                return True

        return False
                
                

        
        
        
         