class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        count_neg = 0
        count_pos = 0

        for index in range(len(nums)):
            
            if nums[index] > 0:
                count_pos += 1
            elif nums[index] < 0:
                count_neg += 1
                
        return max(count_pos , count_neg)