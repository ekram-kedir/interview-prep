# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# ANSWER

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k=Counter(nums)
        ans=[]
        for k,v in k.items():
            if v<=k:
                ans.append(k)
        return ans
