class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = nums
        sufProduct = nums[::-1]
        answer = []
        for num in range(1, len(nums)):
            preProduct[num] *= nums[num - 1]
        
        for num in range(1, len(nums)):
            sufProduct[num] *= sufProduct[num - 1]
        sufProduct = sufProduct[::-1]
        answer.append(sufProduct[1])
        for num in range(1,len(nums) - 1):
            answer.append(preProduct[num - 1] * sufProduct[num + 1])
        answer.append(preProduct[-2])
        return answer
            
            