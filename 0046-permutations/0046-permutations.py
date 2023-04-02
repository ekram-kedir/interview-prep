class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        if len(nums) == 1:
            return [nums.copy()]
        for idx in range(len(nums)):
            first = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(first)
            answer.extend(perms)
            nums.append(first)
            
        return answer