class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if right < len(nums) and nums[right] != target or right == len(nums):
            return -1
        else:
            return right