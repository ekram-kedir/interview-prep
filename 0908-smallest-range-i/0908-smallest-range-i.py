class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        if nums[-1] - nums[0] > k * 2:
            return (nums[-1] - k) - (nums[0] + k)
        else:
            return 0