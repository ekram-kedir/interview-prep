class Solution:
    def minimumSum(self, num: int) -> int:
        
        nums = list(str(num))
        nums.sort()
        new1 = ""
        new2 = ""
        new1 += str(nums[0])
        new1 += str(nums[-1])
        new2 += str(nums[1])
        new2 += str(nums[-2])
        
        return int(new1) + int(new2)