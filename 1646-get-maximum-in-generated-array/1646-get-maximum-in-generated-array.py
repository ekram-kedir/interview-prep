class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        
        nums = [0] * (n + 1)
        
        def dp(idx):
            if idx == 0 or idx == 1:
                return idx
            elif idx % 2 == 0:
                nums[idx] =  dp(idx//2)
            elif idx % 2 != 0:
                nums[idx] =  dp(idx// 2) + dp( idx//2 + 1)
            return nums[idx]
        
        for i in range(n + 1):
            dp(i)
            
        return max(nums)