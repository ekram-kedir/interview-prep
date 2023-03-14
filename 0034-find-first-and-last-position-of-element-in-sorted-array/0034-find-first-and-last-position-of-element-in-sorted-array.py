class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1 , -1]
        left = -1
        right = len(nums)
        
        if right == 0:
            return ans
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if right < len(nums) and nums[right] == target:
            ans[0] = right
            while right < len(nums) - 1 and nums[right] == target:
                if nums[right + 1] == target:
                    right += 1
                else:
                    break
            ans[1] = right
            return ans
        else:
            return ans