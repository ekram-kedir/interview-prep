class Solution:
    def backtrack(self , index , subsequence , nums):
        if len(subsequence) > 1:
            take = tuple(subsequence)
            if take in self.result:
                return
            self.result.add(take)
            
        for idx in range(index, len(nums)):
            if not subsequence or subsequence[-1] <= nums[idx]:
                subsequence.append(nums[idx])
            else:
                continue
                
            self.backtrack(idx + 1 , subsequence , nums)
            subsequence.pop()
            # self.backtrack(idx + 1 , subsequence , nums)
            
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        self.backtrack(0 , [] , nums)
        return self.result