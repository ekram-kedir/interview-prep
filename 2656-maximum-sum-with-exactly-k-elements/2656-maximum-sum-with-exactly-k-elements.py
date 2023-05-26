class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        take = max(nums)
        total = take
        while k > 1:
            total  += take + 1
            take += 1
            k -= 1
        return total