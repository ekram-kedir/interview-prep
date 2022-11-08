class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d=dict()
        d[0]=-1
        prefix=0
        output=0
        for i in range(len(nums)):
            prefix += 1 if nums[i] else -1
            if prefix in d:
                output = max(output, i- d[prefix])
            else:
                d[prefix] = i
        return output