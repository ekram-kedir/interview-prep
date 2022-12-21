class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(0,l):
            l+=(i-nums[i])
        return l