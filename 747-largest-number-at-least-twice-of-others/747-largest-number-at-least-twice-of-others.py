class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ans=max(nums)
        if ans>=2*sorted(nums)[-2]:
            return nums.index(ans)
        return -1