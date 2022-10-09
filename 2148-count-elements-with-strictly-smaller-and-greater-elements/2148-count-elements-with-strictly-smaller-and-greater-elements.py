class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i==min(nums) or i==max(nums):
                count+=1
        return len(nums)-count