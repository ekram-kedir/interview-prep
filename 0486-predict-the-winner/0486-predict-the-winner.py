class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def helper(left, right):

            if left > right : return 0

            choosenLeft = nums[left] - helper(left + 1 ,right)
            choosenRight = nums[right] - helper(left ,right - 1)

            return max(choosenLeft,choosenRight)
        return helper(0 , n - 1) >= 0
    
            