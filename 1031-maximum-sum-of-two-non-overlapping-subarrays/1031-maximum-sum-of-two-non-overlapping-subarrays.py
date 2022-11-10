class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        windowsum = 0
        first, second = 0, 0
        firstmax, secondmax = 0, 0
        while first < len(nums) - firstLen + 1:
            firstmax = sum(nums[first:first + firstLen])
            if secondLen <= first:
                second = 0
                while second + secondLen <= first:
                    secondmax = sum(nums[second:second + secondLen])
                    windowsum = max(windowsum, firstmax + secondmax)
                    second += 1

            if len(nums) - (first + 1) >= secondLen:
                second = 0
                while second + first + secondLen <= len(nums):
                    secondmax = sum(nums[first + second + firstLen:first + second + firstLen + secondLen])
                    windowsum = max(windowsum, firstmax + secondmax)
                    second += 1
            first += 1
        return windowsum
        