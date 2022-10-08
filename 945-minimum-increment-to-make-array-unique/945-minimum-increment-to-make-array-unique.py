class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev=nums[0]
        ans=0
        for i in range(1,len(nums)):
            res=nums[i]
            if res<=prev:
                ans+=prev-res+1
                res=prev+1
            prev=res
        return ans