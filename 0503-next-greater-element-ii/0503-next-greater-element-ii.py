class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1 for i in range(len(nums))]
        inc_stack = []
        nums = nums + nums
        for num in range(len(nums)):
        
            while inc_stack and nums[inc_stack[-1]] < nums[num]:
                answer[inc_stack.pop()] = nums[num]
             
            if num < n:
                inc_stack.append(num)
            else:
                if not inc_stack:break
    
        return answer
    
    