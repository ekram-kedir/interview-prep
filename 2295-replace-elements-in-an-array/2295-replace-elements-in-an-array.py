class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        index_store = {num:i for i,num in enumerate(nums)}
        
        for removed , replaced in operations:
            index = index_store[removed]
            nums[index] = replaced
            index_store[replaced] = index
            del index_store[removed]
        return nums