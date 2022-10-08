class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        return sum(i-nums[0] for i in nums)