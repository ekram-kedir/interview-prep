class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        windowSum = sum(nums[:k])
        maxSum = windowSum
        for num in range(n - k):
            windowSum = windowSum - nums[num] + nums[num + k]
            maxSum = max(windowSum , maxSum)
        return maxSum / k
   