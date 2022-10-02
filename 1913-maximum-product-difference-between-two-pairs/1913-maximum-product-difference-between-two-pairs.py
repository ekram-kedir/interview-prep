class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return (sorted(nums)[-2]*sorted(nums)[-1])-(sorted(nums)[0]*sorted(nums)[1])