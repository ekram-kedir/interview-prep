# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# ANSWER
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,cur_sum=0,0
        ans=float("inf")
        for i in range(len(nums)):
            cur_sum+=nums[i]
            while cur_sum>=target:
                ans=min(ans,i-l+1)
                cur_sum-=nums[l]
                l+=1
        return 0 if ans==float("inf") else ans
