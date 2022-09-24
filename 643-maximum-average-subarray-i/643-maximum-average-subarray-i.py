class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        window_average = window_sum/k
        max_average=window_average
        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            window_average=window_sum/k
            max_average = max(window_average, max_average)
        return max_average
   