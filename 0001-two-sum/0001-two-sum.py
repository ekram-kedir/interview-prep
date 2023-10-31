class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        for right in range(len(nums)):
            for left in range(right + 1 , len(nums)):
                if nums[left] + nums[right] == target:
                    answer.append(right)
                    answer.append(left)
        return answer