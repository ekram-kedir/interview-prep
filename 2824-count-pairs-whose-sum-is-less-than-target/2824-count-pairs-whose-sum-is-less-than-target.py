class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                if 0 <= i < j < len(nums) and nums[i] + nums[j] < target:
                    count += 1
        return count