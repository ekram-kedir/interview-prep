class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z=0
        for i in range(len(nums)):
            if nums[i]:
                nums[z],nums[i]=nums[i],nums[z]
                z+=1
        return nums