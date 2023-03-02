class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ans = [0 for i in range(len(nums))]
        
        for start, end in requests:
            ans[start] += 1
            if end + 1 < len(nums):
                ans[end + 1]  -= 1
        
        for prefix in range(1,len(nums)):
            ans[prefix] += ans[prefix - 1]
            
        ans.sort()
        nums.sort()
        Mod = 10**(9) + 7
        total = 0
        for i in range(len(ans)):
            total += ans[i] * nums[i]
        return total % Mod